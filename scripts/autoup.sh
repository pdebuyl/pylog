#/bin/bash

files=$(git diff-index --name-status --cached HEAD | grep -v ^D | grep "\.py\$" | cut -c3-)

for f in $files
do
    if [[ `grep -c -P "^__version__ = \"\d\.\d\.\d\"\$" "$f"` = 1 ]]
    then
	x=`awk '{FS="[\".]"} {ORS=""} /^__version__/ {{print $2} {exit}}' "$f"`
	y=`awk '{FS="[\".]"} {ORS=""} /^__version__/ {{print $3} {exit}}' "$f"`
	z=`awk '{FS="[\".]"} {ORS=""} /^__version__/ {{print $4} {exit}}' "$f"`
	echo "$x.$y.$z"
	z=$((z+1))
	sed -e "s/__version__ = \"\([[:digit:]]\)\.\([[:digit:]]\)\.\([[:digit:]]\)\"/__version__ = \"$x.$y.$z\"/g" "$f"
	#git add "$f"
    else
	echo "pre-commit fail: file does not contain version line or contains more than one."
	exit 1
    fi
done
