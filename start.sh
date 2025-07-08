#!/bin/bash
reflex init
reflex export --frontend-only
unzip frontend.zip -d .web/public
rm -f frontend.zip
reflex run --env prod --backend-only
