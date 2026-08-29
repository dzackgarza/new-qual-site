---
schema: qual/card@1
id: P-CAFA25B
kind: problem
title: "Punctured disk holomorphic function with |f| <= A|z|^{-3/2} has a simple pole at most"
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Poles
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $f : \{z : 0 < |z| < 1\} \to \mathbb{C}$ be holomorphic and assume that $|f(z)| \leq A|z|^{-3/2}$ for some constant $A$.
Prove that there is a complex constant $\alpha$ such that $g(z) := f(z) - \alpha z^{-1}$ can be extended to a holomorphic function on $\{z : |z| < 1\}$.
:::

::: {.solution}
**Goal.** Show $f$ has at worst a simple pole at $0$, i.e. $f(z) - \alpha z^{-1}$ extends holomorphically across $0$.

<1>1. $f$ has a Laurent expansion $f(z) = \sum_{n=-\infty}^{\infty} a_n z^n$ on $0 < |z| < 1$.
Proof: $f$ is holomorphic on the punctured disk.

<1>2. $a_n = 0$ for all $n \le -2$.
<2>1. For $n \le -2$, $a_n = \frac{1}{2\pi i} \oint_{|z| = r} f(z) z^{-n-1}\, dz$ for any $0 < r < 1$.
Proof: Laurent coefficient formula.
<2>2. $|a_n| \le \frac{1}{2\pi} \cdot 2\pi r \cdot \sup_{|z|=r} |f(z)| \cdot r^{-n-1} \le A r^{-3/2} \cdot r^{-n-1} = A r^{-n - 5/2}$.
Proof: bound the integral by length times sup; use $|f(z)| \le A |z|^{-3/2} = A r^{-3/2}$.
<2>3. For $n \le -2$, $-n - 5/2 \ge -1/2 > 0$, so $A r^{-n-5/2} \to 0$ as $r \to 0^+$.
Proof: the exponent is positive.
<2>4. Hence $a_n = 0$ for $n \le -2$.
Proof: <2>2 and <2>3 force $|a_n| = 0$.

<1>3. Therefore $f(z) = a_{-1} z^{-1} + h(z)$ where $h$ is holomorphic on $|z| < 1$.
Proof: <1>2 removes all terms of order $\le -2$; the remaining nonnegative powers form a holomorphic function $h$ on the full disk.

<1>4. Set $\alpha = a_{-1}$ and $g(z) = f(z) - \alpha z^{-1} = h(z)$.
Proof: definition.

<1>5. $g$ extends holomorphically to $|z| < 1$.
Proof: $g = h$ is holomorphic on the full disk by <1>3.

<1>6. Q.E.D.
Proof: <1>4–<1>5.
:::
