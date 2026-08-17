---
schema: qual/card@1
id: P-3EAU2
kind: problem
title: "Suppose $f$ is analytic on $\\DD^\\circ$. Determine with proof which of the\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - identity-theorem
  - zeros
  - holomorphic-functions
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Suppose $f$ is analytic on $\DD^\circ$.
Determine with proof which of the following are possible:

a. $f\qty{1\over n} = (-1)^n$ for each $n>1$.

b. $f\qty{1\over n} = e^{-n}$ for each even integer $n>1$ while $f\qty{1\over n} = 0$ for each odd integer $n>1$.

c. $f\qty{1\over n^2} = {1\over n}$ for each integer $n>1$.

d. $f\qty{1\over n} = {n-2 \over n-1}$ for each integer $n>1$.

:::

:::{.solution}

**Part a**:
Not possible: if $f$ is holomorphic then $f$ is in particular continuous, so 
\[
f(0) = f(\lim 1/n) = \lim f(1/n) = \lim (-1)^n
,\]
which does not converge.

**Part b**:
Not possible: note that $1/n$ has a limit point, so if $f(1/n)=0$ then $f\equiv 0$ on $\DD$ by the identity principle.
In particular, we can not have $f(1/n) = e^{-n}>0$.

Alternatively, note that a holomorphic $f$ must have isolated zeros, while $z_0=0$ is forced to be a zero of $f$ by continuity, which has infinitely many zeros of the form $1/n$ in any neighborhood.

**Part c**:
Not possible: suppose so, then by continuity, we have
\[
f(0) = f(\lim 1/n^2)= \lim f(1/n^2)=\lim 1/n = 0
,\]
so $z_0=0$ is a zero.
Now defining $g(z) = z^{1\over 2} \da e^{1\over 2 \log(z)}$ on $U \da \CC\sm(-\infty, 0]$ extending this continuously to zero by $g(0)= 0$ yields $g(z) = f(z)$on $\ts{1/n^2 \st n>1}\union\ts{0}$, so $g(z) \equiv f(z)$ on $U$.
But then $g\equiv f$ on $\DD$, and $g$ is not holomorphic on all of $\D$, contradicting that $f$ was holomorphic on $\DD$.

**Part d**:
Yes: note that this forces $f(0) = \lim {n-2\over n-1} = 1$ by continuity at $z=0$.
We can write 
\[
{n-2\over n-1} = {1 - 2\cdot{1\over n} \over 1 - {1\over n}}
,\]
so define $g(z) \da {1-2z\over 1-z}$.
Then $g(1/n) = f(1/n)$ for all $n$ and $g(0) = 1= f(0)$, so $g=f$ on a set with an accumulation point making $g\equiv f$ on $\DD$.
Note that $g$ *is* holomorphic on $\DD$, since it has only a simple pole at $z_0 = 1$.
:::

