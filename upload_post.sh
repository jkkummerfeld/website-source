#!/bin/bash

hugo 
pushd public 
rm post/*/*.bak 
git add . 
git commit 
git push 
popd 

git add content/post/*md 
git add public
git commit 
git push

