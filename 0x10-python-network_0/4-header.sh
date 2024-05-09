#!/bin/bash
# script to send custom headers to servers
curl -s "$1" -H "X-School-User-Id: 98"
