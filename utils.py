"""Utility functions for RTSP camera management."""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


def validate_rtsp_url(url: str) -> bool:
    """Validate RTSP URL format."""
    if not url:
        return False
    return url.startswith('rtsp://')


def format_camera_info(camera) -> str:
    """Format camera information."""
    status = "connected" if camera.is_connected else "disconnected"
    return f"Camera[{camera.camera_id}] {camera.name} - {status}"


def calculate_fps(frame_count: int, elapsed_time: float) -> float:
    """Calculate FPS from frame count and elapsed time."""
    if elapsed_time <= 0:
        return 0.0
    return frame_count / elapsed_time