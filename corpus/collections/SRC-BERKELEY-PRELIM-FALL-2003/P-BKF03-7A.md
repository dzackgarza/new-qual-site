---
schema: qual/card@1
id: P-BKF03-7A
kind: problem
title: Berkeley Fall 2003 prelim problem 7A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Cayley transform, principal-log branch, harmonicity, continuity on the punctured closed disk, and boundary values.
---

::: {.problem}
Let
\[
D=\{z\in\mathbb C:|z|\le 1\}\setminus\{1,-1\}.
\]
Find an explicit continuous function $f:D\to\mathbb R$ satisfying all the following conditions:

- $f$ is harmonic on the interior of $D$ (the open unit disk),

- $f(z)=1$ when $|z|=1$ and $\operatorname{Im}(z)>0$, and

- $f(z)=-1$ when $|z|=1$ and $\operatorname{Im}(z)<0$.
:::
\n\n::: {.solution}\nDefine\n\[\nw(z):=\frac{1+z}{1-z}\n\]\nand let $\Log$ be the principal logarithm on $\mathbb C\setminus(-\infty,0]$.
Set\n\[\n\boxed{f(z)=\frac{2}{\pi}\operatorname{Im}\Log\!\left(\frac{1+z}{1-z}\right)}.\n\]\n\n<1>1. The formula is well-defined and continuous on $D$.\n::: {.proof}\nFor $|z|<1$,\n\[\n\operatorname{Re}w(z)=\frac{1-|z|^2}{|1-z|^2}>0,\n\]\nso $w(z)$ lies in the open right half-plane.
For $|z|=1$ with $z\ne\pm1$, one has $\operatorname{Re}w(z)=0$, while $w(z)\ne0$ because $z\ne-1$.
Thus\n\[\nw(D)\subset \{\operatorname{Re}w\ge0\}\setminus\{0\},\n\]\nwhich is contained in the domain of the principal logarithm.
Since $z=1$ is also removed, the denominator never vanishes on $D$.
Therefore $\Log\circ w$ and hence $f$ are continuous on $D$.\n:::\n\n<1>2. The function $f$ is harmonic on the open unit disk.\n::: {.proof}\nOn $|z|<1$, the map $w$ takes values in the open right half-plane, where the principal logarithm is holomorphic.
Thus\n\[\nF(z):=\Log w(z)\n\]\nis holomorphic on the disk.
The imaginary part of a holomorphic function is harmonic, so $f=(2/\pi)\operatorname{Im}F$ is harmonic there.\n:::\n\n<1>3. On the upper boundary semicircle, $f=1$, and on the lower boundary semicircle, $f=-1$.\n::: {.proof}\nWrite $z=e^{i\theta}$ with $0<\theta<2\pi$ and $\theta\ne\pi$.
Then\n\[\nw(e^{i\theta})\n=\frac{1+e^{i\theta}}{1-e^{i\theta}}\n=i\cot\frac{\theta}{2}.\n\]\nIf $0<\theta<\pi$, then $\cot(\theta/2)>0$, so $w(z)$ lies on the positive imaginary axis.
Hence its principal argument is $\pi/2$, and\n\[\nf(z)=\frac2\pi\cdot\frac\pi2=1.\n\]\nIf $\pi<\theta<2\pi$, then $\cot(\theta/2)<0$, so $w(z)$ lies on the negative imaginary axis.
Its principal argument is $-\pi/2$, and therefore\n\[\nf(z)=\frac2\pi\cdot\left(-\frac\pi2\right)=-1.\n\]\nThese are exactly the required boundary values.\n:::\n:::\n
