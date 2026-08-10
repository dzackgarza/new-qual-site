---
schema: qual/card@1
id: P-LF4NL
kind: problem
title: "5. Let $\\delta = \\min\\theset{\\frac 1 2, \\sqrt{\\frac \\varepsilon 2}}$,\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
5. Let $\delta = \min\theset{\frac 1 2, \sqrt{\frac \varepsilon 2}}$, then 
$$\abs{x-1} < \frac 1 2 \implies \frac 1 2 < x < \frac 3 2 \implies \abs{x} > \frac 1 2 \implies \frac 1 {\abs x} < 2$$ and so
  $$\begin{align*}
  \abs{x-1} < \delta \implies \abs{\frac{x^2+1}{x} - 2} 
  &= \abs{\frac{(x-1)^2}{x}} \\
  &= \frac{\abs{x-1}^2}{\abs{x}} \\
  &< 2{\abs{x-1}^2} \\
  &< 2{\delta^2} \\
  &= 2 \left(\frac{\varepsilon} 2\right) \\ 
  &= \varepsilon. \qed
  \end{align*}$$

