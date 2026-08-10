---
schema: qual/card@1
id: P-L3LHW
kind: problem
title: "1. We need to show"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
1. We need to show
    $$
    \forall \varepsilon \exists \delta(\varepsilon) \suchthat \quad \abs{x-2} < \delta \implies \abs{\frac 1 {3+x} - \frac 1 5} < \varepsilon
    $$

    Choose $\delta = 20 \varepsilon$. Then note that we can take $1 < x < 3$, and so $\abs{5(3+x)} < 20$. Then
    $$
    \abs{\frac 1 {3+x} - \frac 1 5} = \abs{\frac{x-2}{5(3+x)}} < \frac 1 {20} \abs{x-2} < \frac 1 {20} (20 \varepsilon) < \varepsilon. \qed
    $$

