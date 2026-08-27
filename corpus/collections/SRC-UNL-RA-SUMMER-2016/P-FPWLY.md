---
schema: qual/card@1
id: P-FPWLY
kind: problem
title: $f(0)=f(2)=0$ and $f(c)=1$ imply $|f'|>1$ somewhere on $(0,2)$
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

Suppose that $f \colon [0,2] \to \mathbb{R}$ is continuous on $[0,2]$ , differentiable on $(0,2)$, and such that $f(0) = f(2) = 0$, $f(c) = 1$ for some $c \in (0,2)$.
Prove that there exists $x \in (0,2)$ such that $|f'(x)| >1.$

::: {.proof}
*Proof.* We will consider three cases.
First, suppose $c<1$.
Then, by the mean value theorem, there exists $x\in (0,c)$ such that $f'(x)(c-0)=f(c)-f(0)$ so $f'(x)=\frac{f(c)}{c}=\frac{1}{c}>1$ since $c<1$.
Similarly, if $c>1$ then by the mean value theorem there exits $y\in (c,2)$ such that $$|f'(y)|=\left\lvert\frac{f(2)-f(c)}{2-c}\right\rvert=\left\lvert \frac{-f(c)}{2-c}\right\rvert=\left\lvert\frac{-1}{2-c}\right\rvert>1$$ since $1<c<2$.

Now, suppose $c=1$.
If there exists $x\in (0,1)$ such that $x<f(x)$ then by the mean value theorem on the interval $(0,x)$ there exists $s\in (0,x)$ such that $f'(s)=\frac{f(x)}{x}>1$ since $f(x)>x$.
Likewise, if there exists $x\in (0,1)$ such that $x>f(x)$ then the mean value theorem on $(x,1)$ gives a point $t\in (x,1)$ such that $\left\lvert f'(t)\right\rvert=\left\lvert \frac{f(1)-f(x)}{1-x}\right\rvert=\left\lvert\frac{1-f(x)}{1-x}\right\rvert>1$ since $x>f(x)$.
So, on $(0,1)$, if the proposition does not hold then $f(x)=x$.
Similarly, if there exists $x\in (1,2)$ such that $f(x)>2-x$ then the mean value theorem yields a point $u\in (x,2)$ such that $|f'(u)|=\left\lvert \frac{f(2)-f(x)}{2-x}\right\rvert=\left\lvert \frac{-f(x)}{2-x}\right\rvert>1$ since $f(x)>2-x$.
If there exists $y\in (1,2)$ such that $f(y)<2-y$ then again by the mean value theorem there exists $v\in (1,y)$ such that $|f'(v)|=\left\lvert\frac{f(y)-f(1)}{y-1}\right\rvert=\left\lvert\frac{f(y)-1}{y-1}\right\rvert>1$ since $f(y)<2-y$ so $|f(y)-1|>|y-1|$.
So, on $(1,2)$ if the proposition does not hold then $f(x)=2-x$.
However, notice that since $f(x)$ is differentiable at $x=1$ we cannot have $f(x)=x$ on $(0,1)$ and $f(x)=2-x$ on $(1,2)$.
◻
:::
::: {.solution}
<1>1. Setup: $f$ continuous on $[0,2]$, differentiable on $(0,2)$, $f(0) = f(2) = 0$, and $f(c) = 1$ for some $c \in (0,2)$.
(The card already contains a complete case-analysis proof; this solution restates it in structured form.)
Proof: given.

<1>2. If $c < 1$: there is $x \in (0, c)$ with $f'(x) = \frac{f(c) - f(0)}{c - 0} = \frac{1}{c} > 1$.
Proof: Mean Value Theorem on $[0, c]$; since $0 < c < 1$, $1/c > 1$.

<1>3. If $c > 1$: there is $y \in (c, 2)$ with $|f'(y)| = \left|\frac{f(2) - f(c)}{2 - c}\right| = \left|\frac{-1}{2-c}\right| = \frac{1}{2-c} > 1$.
Proof: Mean Value Theorem on $[c, 2]$; since $0 < 2 - c < 1$, $1/(2-c) > 1$.

<1>4. It remains to handle $c = 1$.
<2>1. If for some $x \in (0,1)$, $f(x) > x$: then $f'(s) = \frac{f(x) - f(0)}{x - 0} = \frac{f(x)}{x} > 1$ for some $s \in (0, x)$.
Proof: Mean Value Theorem on $[0, x]$; $f(x) > x$ gives $f(x)/x > 1$.
<2>2. If for some $x \in (0,1)$, $f(x) < x$: then $|f'(t)| = \left|\frac{f(1) - f(x)}{1 - x}\right| = \left|\frac{1 - f(x)}{1 - x}\right| > 1$ for some $t \in (x, 1)$.
Proof: Mean Value Theorem on $[x, 1]$ (note $f(1) = f(c) = 1$); $f(x) < x$ implies $1 - f(x) > 1 - x > 0$, so the ratio is $> 1$.
<2>3. Hence, unless we are already done, $f(x) = x$ for all $x \in (0,1)$.
Proof: <2>1 and <2>2 exhaust $f(x) > x$ and $f(x) < x$.
<2>4. Similarly on $(1, 2)$: unless done, $f(x) = 2 - x$ for all $x \in (1,2)$.
Proof: if $f(x) > 2 - x$ for some $x \in (1,2)$, MVT on $[x,2]$ gives $|f'(u)| = \left|\frac{f(2) - f(x)}{2-x}\right| = \frac{f(x)}{2-x} > 1$; if $f(x) < 2 - x$, MVT on $[1, x]$ gives $|f'(v)| = \left|\frac{f(x) - f(1)}{x - 1}\right| = \frac{|f(x) - 1|}{x-1} > 1$ since $|f(x) - 1| > |x - 1|$.
<2>5. $f(x) = x$ on $(0,1)$ and $f(x) = 2 - x$ on $(1,2)$ contradict differentiability at $1$.
Proof: the left derivative of $x$ at $1$ is $1$, the right derivative of $2 - x$ at $1$ is $-1$; they differ, so $f$ is not differentiable at $1$.

<1>5. Q.E.D.: in every case some $x \in (0,2)$ has $|f'(x)| > 1$.
Proof: <1>2, <1>3, and <1>4 (cases $c < 1$, $c > 1$, $c = 1$) are exhaustive.
:::
