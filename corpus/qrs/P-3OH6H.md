---
schema: qual/card@1
id: P-3OH6H
kind: problem
title: "2. Claim: take $\\delta < \\min(1, \\sqrt{\\frac{\\varepsilon}{5}})$. Then\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
2. Claim: take $\delta < \min(1, \sqrt{\frac{\varepsilon}{5}})$. Then $\abs{x-2} < \delta \implies 1 < x < 2 \implies 1 > \frac 1 x > \frac 1 2$, so in particular $\frac 1 x < 1$ and
   $$\begin{align*}
   \abs{x + \frac 1 x - \frac 5 2} &= \abs{\frac{2x^2 - 5x + 2}{2x}}\\
   &< \frac 1 2 \abs{(2x^2-4x + 2) - x}\\
   &= \frac 1 2 \abs{2(x-2)^2 + 3(x-2)} \\
   &< \abs{2(x-2)^2 + 3(x-2)} \\
   &\leq 2\abs{x-2}^2 + 3\abs{x-2} \\
   &< 2\delta^2 + 3\delta \\ 
   &< 5\delta^2  \hspace{10em} \text{since } \delta < 1 \implies \delta^2 < \delta \\
   &< 5 \left(\sqrt{\frac{\varepsilon}{5}}\right)^2 \\
   &= \varepsilon.
   \end{align*}$$
   $\qed$

