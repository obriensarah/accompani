printf "Building accompani...\n\n"
  
yarn build

printf "\n\nBuild complete. Optimized version ready to release.\n\n"

printf "\n\n Syncing to S3...\n\n"

aws s3 cp --recursive build s3://accompani.io --profile ryanmchenry2

printf "\n\nSync complete - s3 is up to date.\n\n"

# aws cloudfront create-invalidation --profile ryanmchenry2 --distribution-id E1MJG1CD11L03K --paths /
#echo "cloudfront invalidation of caches complete."


echo "Release complete!"
