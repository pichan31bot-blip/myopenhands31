"""Main entry point for RTSP multi-camera streaming."""

import sys
import logging
import time
from streaming import StreamManager
from utils import validate_rtsp_url, format_camera_info
from camera import GROUP_7


def main():
    """Main function."""
    print(f"Starting {GROUP_7} RTSP Camera System")

    manager = StreamManager()

    # Example camera configurations
    cameras_config = [
        ("Camera_1", "rtsp://example.com/stream1", 1),
        ("Camera_2", "rtsp://example.com/stream2", 2),
        ("Camera_3", "rtsp://example.com/stream3", 3),
    ]

    # Add cameras
    for name, url, camera_id in cameras_config:
        if validate_rtsp_url(url):
            manager.add_camera(name, url, camera_id)

    # Connect to all cameras
    if not manager.connect_all():
        print("Failed to connect to some cameras")
        sys.exit(1)

    print(f"Connected to {manager.get_camera_count()} cameras")

    # Start streaming
    manager.start_all()

    try:
        while True:
            frames = manager.get_all_frames()
            if frames:
                print(f"Processing {len(frames)} frames...")
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        manager.stop_all()


if __name__ == "__main__":
    main()