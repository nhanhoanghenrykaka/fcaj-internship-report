---
title: "S3 and CloudFront for the frontend"
date: 2026-06-15
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

# 5.4.3. Deploy the frontend with S3 and CloudFront

## 1. Build the frontend

From the frontend directory:

```bash
npm ci
npm run build
```

Review build-time environment variables. When CloudFront provides one public domain, the frontend should use a path such as `/api` instead of a hard-coded `localhost` URL.

## 2. Create a private S3 bucket and upload artifacts

1. Create a globally unique bucket name.
2. Keep **Block Public Access** enabled.
3. Upload the contents of the `dist` directory.
4. Do not expose objects through public ACLs.

The build can be synchronized with AWS CLI:

```bash
aws s3 sync dist/ s3://<frontend-bucket> --delete
```



![S3 bucket containing the frontend build](images/5-Workshop/s3_bucket.jpg?featherlight=false)
*Figure 1. The S3 bucket stores artifacts produced by `npm run build`, including `index.html`, JavaScript, CSS, and React/Vite static assets.*

## 3. Create the CloudFront distribution

Configure the distribution as follows:

- use the S3 bucket as the default origin;
- use Origin Access Control so CloudFront can read the private bucket;
- set the default root object to `index.html`;
- configure SPA fallback for client-side routes;
- add the ALB as a second origin;
- add an `/api/*` behavior that forwards required methods, headers, and query strings to the ALB;
- do not apply static-content caching rules to dynamic API traffic.



![CloudFront distribution delivering the frontend](images/5-Workshop/fe_cloudfront.jpg?featherlight=false)
*Figure 2. The CloudFront distribution provides an HTTPS domain, retrieves frontend assets from S3, and can route the `/api/*` behavior to the ALB.*

## 4. Validate the frontend and API

1. Open the CloudFront domain.
2. Refresh a nested route to test SPA fallback.
3. Sign in and call an API through the same domain.
4. Use the browser Network panel to confirm that requests no longer target `localhost`.
5. Review CORS settings when the frontend and API use different domains.

## 5. Release a new frontend version

Create an invalidation when old files remain cached after a new upload:

```bash
aws cloudfront create-invalidation \
  --distribution-id <distribution-id> \
  --paths "/*"
```

In production, content-hashed assets reduce invalidation requirements; `index.html` normally uses a shorter cache policy than hashed assets.
