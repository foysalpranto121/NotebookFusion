from IPython import display

# ADDED: For making HTTP requests
import urllib.request

# ADDED: Specific URL-related exceptions
import urllib.error

# ADDED: Parse and normalize URLs
from urllib.parse import urlparse

# ADDED: Handle timeout exceptions
import socket

# ADDED: Measure response/load time
import time

from NotebookFusion.custom_exception import InvalidURLException
from NotebookFusion.logger import logger


# ADDED: Global timeout configuration
DEFAULT_TIMEOUT = 10


# ADDED FUNCTION
# Purpose:
# Automatically adds https:// if user enters only domain
# Example:
# google.com -> https://google.com
def normalize_url(url: str) -> str:
    """
    Automatically add https:// if scheme is missing
    """

    # ADDED: Parse URL structure
    parsed = urlparse(url)

    # ADDED: Check if scheme exists
    if not parsed.scheme:

        # ADDED: Add HTTPS automatically
        url = f"https://{url}"

    return url


# UPDATED FUNCTION
# Added:
# - timeout handling
# - metadata return
# - response time measurement
# - content-type extraction
# - better logging
# - browser headers
def is_valid(
    url: str,

    # ADDED: Configurable timeout
    timeout: int = DEFAULT_TIMEOUT,

    # ADDED: Future extensibility
    allow_redirects: bool = True,
) -> tuple:
    """
    Validate URL and return metadata
    """

    try:

        # ADDED: Normalize URL first
        url = normalize_url(url)

        # ADDED: Browser-like headers
        # Some websites block requests without User-Agent
        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"
            )
        }

        # ADDED: Create request object
        request = urllib.request.Request(
            url,
            headers=headers
        )

        # ADDED: Start timer
        start_time = time.time()

        # UPDATED:
        # Added timeout support
        response = urllib.request.urlopen(
            request,
            timeout=timeout
        )

        # ADDED: Calculate response time
        response_time = round(
            time.time() - start_time,
            2
        )

        # ADDED: Extract status code
        status_code = response.getcode()

        # ADDED: Extract content type
        content_type = response.headers.get(
            "Content-Type"
        )

        # UPDATED: Better logging
        logger.info(
            f"URL Validated | "
            f"Status: {status_code} | "
            f"Response Time: {response_time}s"
        )

        # UPDATED:
        # Returning metadata dictionary
        return (
            True,
            {
                "url": url,
                "status_code": status_code,
                "content_type": content_type,
                "response_time": response_time,
            }
        )

    # ADDED: Handle HTTP-specific errors
    except urllib.error.HTTPError as e:
        logger.error(
            f"HTTP Error: {e.code} - {e.reason}"
        )

    # ADDED: Handle invalid URLs/domain issues
    except urllib.error.URLError as e:
        logger.error(
            f"URL Error: {e.reason}"
        )

    # ADDED: Handle timeout errors
    except socket.timeout:
        logger.error("Request timed out")

    # UPDATED: General exception logging
    except Exception as e:
        logger.exception(e)

    # UPDATED:
    # Return consistent structure
    return (False, {})


# UPDATED FUNCTION
# Added:
# - metadata display
# - timeout configuration
# - structured return
# - better error handling
def render_site(
    url: str,

    # Existing
    width: str = "100%",
    height: str = "600",

    # ADDED: Timeout control
    timeout: int = DEFAULT_TIMEOUT,

    # ADDED: Toggle metadata printing
    show_metadata: bool = True,
) -> dict:
    """
    Render website inside notebook
    """

    try:

        # UPDATED:
        # Get validation + metadata
        is_ok, metadata = is_valid(
            url,
            timeout=timeout
        )

        # UPDATED:
        # Better custom exception message
        if not is_ok:
            raise InvalidURLException(
                f"Invalid or unreachable URL: {url}"
            )

        # Existing iframe rendering
        iframe = display.IFrame(
            src=metadata["url"],
            width=width,
            height=height,
        )

        # Existing display rendering
        display.display(iframe)

        # ADDED:
        # Show metadata information
        if show_metadata:

            print("=== Website Metadata ===")

            for key, value in metadata.items():
                print(f"{key}: {value}")

        # ADDED:
        # Structured success response
        return {
            "status": "success",
            "metadata": metadata
        }

    # UPDATED:
    # Better exception logging
    except Exception as e:
        logger.exception(e)
        raise