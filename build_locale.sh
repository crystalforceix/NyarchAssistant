fd -t f -e py src | xargs rg -l "_\(|N\(_" >po/POTFILES
fd -t f '.*\.xml$|.*\.in$' data >>po/POTFILES
xgettext -o po/waifuassistant.pot $(cat po/POTFILES)
cd po
for file in $(fd -e po); do
	msgmerge -U "$file" waifuassistant.pot
done
rm -f *~
