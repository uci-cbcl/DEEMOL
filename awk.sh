#!/bin/bash

awk -F'\t' '($4 ~ /^VCAP$/) && ($5 ~ /^24\.0$/) && ($9 ~ /^b/) && ($10 ~ /^r2$/) && ($11 ~ /^dp52,dp53$/) && ($14 ~ /^duo$/) && ($24 ~ /^trt_cp$/) && ($26 ~ /^epsilon$/)  {print $0}'  $1


