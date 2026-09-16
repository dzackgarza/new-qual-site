---
schema: qual/card@1
id: PR-Y36BS
kind: proposition
title: Linear approximation criterion for complex differentiability, and continuity
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Continuity
relations: []
review: draft
---

::: {.proposition}
Let $f$ be defined on a neighborhood of $z_0\in\CC$.
Then $f$ is [[D-E7A5W|holomorphic]] at $z_0$ if and only if there exist $a\in\CC$ and a function $\psi$ defined for small $h\neq0$ such that
$$
f(z_0+h)-f(z_0)-ah=h\,\psi(h),\qquad \psi(h)\to0\text{ as }h\to0.
$$
In this case $a=f'(z_0)$, and $f$ is continuous at $z_0$.
:::

::: {.proof}
If $f'(z_0)$ exists, put $a\coloneqq f'(z_0)$ and $\psi(h)\coloneqq\frac{f(z_0+h)-f(z_0)}{h}-a$, which tends to $0$.
Conversely, dividing the displayed identity by $h$ gives $\frac{f(z_0+h)-f(z_0)}{h}=a+\psi(h)\to a$, so $f'(z_0)=a$.
Finally $f(z_0+h)-f(z_0)=h\big(a+\psi(h)\big)\to0$ as $h\to0$.
:::
