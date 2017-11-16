#!/bin/bash

find . -name "*.bak" | xargs rm

hugo 
pushd public
git add . 
git commit 
git push 
popd 

git add content/post/*md 
git add public
git commit 
git push

