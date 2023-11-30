# AIApp-report

## Install

```bash
pip install googletrends httpx
```

## Product Hunt Analysis
Reference: [thenextweb](https://thenextweb.com/news/much-needed-research-shows-effectively-launch-product-product-hunt), [gigasheet](https://www.gigasheet.com/post/product-hunt-data-download)
1. Using Product Hunt API, gathering info about `publication, images, videos, tags, upvotes, interests of hunters, and position in the ranking , maybe also comments?`
1. Because of this, it was useless to compare products by their absolute position in the ranking. To overcome the problem, researchers calculated the project’s proximity to the best ranked – calculating the percentage of gained engagement in relation to the day’s best-ranked.
1. In order to analyze only relevant data, Popsters filtered out products whose websites reported errors (404, 500,…), outdated SSL, redirection to hosting services, or outdated footers (2014 being the earliest year accepted). Additionally, it didn’t consider products whose websites had a views count below 5000
1. Time considered is always Pacific Standard Time
1. Those remained were additionally filtered based on the traffic data from SimilarWeb: we screened out the projects which had the supposed visits count below 5000.