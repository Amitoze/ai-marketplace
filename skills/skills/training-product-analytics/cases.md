# Case library

Published cases and guides to base hidden truths on and to cite in
debriefs. Compiled 2026-11-24 from web searches.

**Status column.** `found` = surfaced in search with a matching summary;
the page itself was not opened. `read` = page opened and checked.
`memory` = known from memory only, link not confirmed. Open a source and
upgrade its status before quoting from it. Add new cases as they are
used; never delete a row, mark it dead instead.

## Type 1: diagnose a metric change

| Source | What it shows | Tag | Status |
|---|---|---|---|
| Sequoia, "Analyzing metric changes" series https://articles.sequoiacap.com/analyzing-metric-changes-part-vii-action-plan | pick two time points; split a change into parts step by step | `[third-party]` | found |
| Meta research, automated root cause analysis (2021) https://research.facebook.com/blog/2021/07/automating-root-cause-analysis-for-infrastructure-systems/ | drill down by country, app, device to find the cut holding the drop | `[company]` | found |
| Yammer engagement-drop case (Mode); write-up https://towardsdatascience.com/yammer-investigating-a-sudden-drop-in-user-engagement-7c9c4093c038 | a worked engagement-drop investigation on a public dataset | `[third-party]` | found |
| Interview Query, metrics drop guide https://www.interviewquery.com/p/metrics-drop-data-science-interview | check it is real, then scope, then causes | `[third-party]` | found |
| Statsig, why metrics changed https://www.statsig.com/perspectives/diagnostic-analytics-metrics-change | ask engineering about releases on the date | `[vendor-benchmark]` | found |

## Type 2: define success measures

| Source | What it shows | Tag | Status |
|---|---|---|---|
| Mixpanel, metrics strategy best practices https://mixpanel.com/blog/metric-trees-best-practices/ | focus metric = value moment + natural frequency; inputs a team controls | `[vendor-benchmark]` | read |
| Count, metric trees advice https://count.co/blog/metric-trees---advice-and-best-practice | splits must add up; dotted lines for unproven links | `[third-party]` | read |
| Lenny's Newsletter, determining your activation metric https://www.lennysnewsletter.com/p/how-to-determine-your-activation | list candidates, test which predict retention, then test cause | `[third-party]` | found |
| Duolingo, growth model blog post | active users split into states; one retention rate found to matter most | `[company]` | memory |
| a16z, 16 Startup Metrics https://a16z.com/16-startup-metrics/ | business versus product measures; paid versus blended cost per customer | `[third-party]` | found |

## Type 3: design an experiment

| Source | What it shows | Tag | Status |
|---|---|---|---|
| Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments* (2020) | the standard text: main measure, guardrails, unit, health checks | `[peer-reviewed]` | memory |
| Kohavi et al., "Trustworthy online controlled experiments: five puzzling outcomes explained" (KDD 2012) | surprising results traced to root causes | `[peer-reviewed]` | found |
| Kohavi et al., "Unexpected results in online controlled experiments" (2010) | ten surprises; failed identical-versus-identical tests | `[peer-reviewed]` | found |
| Kohavi, Deng, Vermeer, "A/B Testing Intuition Busters" (KDD 2022) | distrust big wins from small tests; replicate | `[peer-reviewed]` | found |
| Dmitriev et al., "Pitfalls of long-term online controlled experiments" | long tests can mislead for their own reasons | `[peer-reviewed]` | found |
| Li, Zhao, Johari, Weintraub, marketplace interference (2022) https://arxiv.org/abs/2104.12222 | two user groups competing bias the result; which side to randomise | `[peer-reviewed]` | found |

## Type 4: measure impact with no experiment

| Source | What it shows | Tag | Status |
|---|---|---|---|
| Buffer, price change analysis https://bufferapp.github.io/analysis/awesome_price_change_analysis.html | a real subscription price change judged against a forecast | `[company]` | found |
| Teconomics, "5 tricks when A/B testing is off the table" https://medium.com/teconomics-blog/5-tricks-when-ab-testing-is-off-the-table-f2637e9f15a5 | menu of methods and when each fits | `[third-party]` | found |
| Kohavi, Tang, Xu, chapter 11, observational causal studies | where each method sits below an experiment | `[peer-reviewed]` | memory |
| Netflix, survey of causal inference applications | country-level campaigns judged with a built comparison group | `[company]` | found via roundup |

## Type 5: trade-off or launch decision

| Source | What it shows | Tag | Status |
|---|---|---|---|
| Kohavi and Thomke, "The surprising power of online experiments" (HBR 2017) | business cases where the decision ran against intuition | `[third-party]` | found |
| RevenueCat, on lifetime value to acquisition cost https://www.revenuecat.com/blog/growth/ltv-cac-subscription-apps-alternatives | why one ratio misleads; payback and cohorts instead | `[vendor-benchmark]` | found |
| DZone, marketplace testing interference https://dzone.com/articles/marketplace-ab-testing-interference | a gain can be moved from elsewhere, not created | `[third-party]` | found |

## Gaps

No company write-up was found of a launch held back because a guardrail
moved. No pricing case from a large consumer company using a comparison
group was found. Search these again before relying on type 4 or 5 cases.
