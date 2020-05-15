#!/usr/bin/env bash
set -e

# Test display value
echo "HOST_ALIAS: ${HOST_ALIAS}"
echo "ACCESS_KEY: ${ACCESS_KEY}"
echo "SECRET_KEY: ${SECRET_KEY}"
echo "BUCKET: ${BUCKET}"
echo "DEST_FOLDER: ${DEST_FOLDER}"
echo "CRON: ${CRON} minute"

LOOPING=$((CRON * 5))

echo "Add host"
/usr/bin/mc config host add ${HOST_ALIAS} https://storage.googleapis.com ${ACCESS_KEY} ${SECRET_KEY}

echo "Running job every $LOOPING seconds"
while true; do	
	# sleep ${LOOPING}
	seconds=$(( $(date -u +%s) % LOOPING))
	[[ $seconds -lt 1 ]] || sleep $((LOOPING - seconds))

	echo "Start mirorring ${HOST_ALIAS}"	
	/usr/bin/mc mirror --overwrite ${HOST_ALIAS}/${BUCKET} ${DEST_FOLDER}
	echo "Finish mirorring ${HOST_ALIAS}"

done
# echo "${CRON} mc mirror --overwrite ${HOST_ALIAS} ${DEST_FOLDER}" > /etc/crontabs/root