---
schema: qual/card@1
id: P-AMD-YDNWHPDM
kind: problem
title: "Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show that $2^{n-1} \\sin\\frac{\\pi}{n} \\sin\\frac{2\\pi}{n} \\cdots \\sin\\frac{(n-1)\\pi}{n} = n \\;$\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
    that
    $$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
    = n
    \; .$$ 
    
    > Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.

    (a) Show that in polar coordinates, the Cauchy-Riemann
    equations take the form

    $$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
    \; \; \; \text{and} \; \; \;
    \frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$

    (b) Use these equations to show that the logarithm function
    defined by $$\log z = \log r + i \theta \; \;
    \mbox{where} \; z = r e^{i \theta } \; \mbox{with} \; - \pi < \theta < \pi$$
    is a holomorphic function in the region
    $r>0, \; - \pi < \theta < \pi$. Also show that $\log z$ defined
    above is not continuous in $r>0$.
:::
