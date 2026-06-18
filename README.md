# Coach Knux

**Your AI striking coach.**

Coach Knux is an AI-powered Muay Thai coaching platform that analyzes training videos using pose estimation, form evaluation, and regression-tested computer vision.

The long-term vision is to help athletes train smarter at home by turning uploaded videos and live webcam sessions into clear, measurable coaching feedback.

## Current Status

Ugly v0 shipped.

Current version includes:

- Basic Python project structure
- Streamlit app shell
- Geometry helper functions for distance, midpoint, and angle calculations
- Unit tests for core math utilities
- Initial setup for future pose estimation and form analysis

## Product Vision

Coach Knux will eventually support three main training modes:

### 1. Upload Video Analysis

Users upload a Muay Thai training video. Coach Knux analyzes the footage and returns a coaching report.

Planned feedback includes:

- Guard drops
- Chin exposure
- Slow hand return
- Weak hip rotation
- Poor stance balance
- Incomplete punch or kick mechanics

### 2. Live Webcam Coach

Users train in front of their MacBook webcam and receive real-time feedback while shadowboxing.

Planned live feedback includes:

- Hands up / hands down status
- Chin tucked / chin exposed status
- Hip rotation feedback
- Combo timing feedback
- Round timer
- Score updates

### 3. Combo Challenge Mode

A Dance Dance Revolution-style Muay Thai training mode.

Coach Knux will show example combos for users to perform in front of the webcam, then score their performance.

Example combo:

```text
Jab → Cross → Lead Hook → Rear Kick