---
schema: qual/card@1
id: P-FPWLY
kind: problem
title: Suppose that $f \colon [0,2] \to \mathbb{R}$ is continuous on
classification:
  areas:
  - real-analysis
  topics:
  - mean-value-theorem
  - differentiation
relations: []
review: draft
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
