---
schema: qual/card@1
id: P-MOL6S
kind: problem
title: $n$th derivative of $xe^{2x}$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $f:\mathbb R\to\mathbb R$ be defined by $f(x)=xe^{2x}$. Find a general formula for the $n$th derivative $f^{(n)}(x)$, and prove it by induction.
:::

::: solution
1. Denoting $D^n f \definedas \dd{^n f}{x^n}$ and noting that $D^1 D^n f = D^{n+1}f$, we have
  $$\begin{align*}
  D^0f &= xe^{2x} \\
  D^1f &= e^{2x} + 2D^0f \\
  D^2f &= 2e^{2x} + 2D^1f \\
  D^3f &= 4e^{2x} + 2D^2f \\
  \end{align*}$$

    and (claim) so we find that 
  $$D^n f = 2^{n-1}e^{2x} + 2D^{n-1}f.$$
  
    This is trivially the case for $n=1$, where we've computed $D^1 f = e^2x + 2xe^{2x} = 2^0e^{2x} + 2D^0 f$, and the inductive step holds exactly because 
  $$
  D^{n+1}f = DD^{n}f \\
  = D(2^{n-1}e^{2x} + 2D^{n-1}f) \\
  =2^n e^{2x} + 2D^n f.
  $$
  $\qed$
:::

::: {.solution}
**Goal:** Find a closed formula for the $n$-th derivative $f^{(n)}(x)$ of $f(x) = x e^{2x}$ for all integers $n \ge 0$, and prove it by induction.

<1>1. Claim: For all $n \ge 0$, $f^{(n)}(x) = (2^n x + n 2^{n-1}) e^{2x}$.
    ::: {.proof}
    By mathematical induction on $n$.
    :::

<1>2. Base Case ($n = 0$): $f^{(0)}(x) = f(x) = (2^0 x + 0 \cdot 2^{-1}) e^{2x} = x e^{2x}$.
    ::: {.proof}
    Direct substitution: $2^0 = 1$ and $0 \cdot 2^{-1} = 0$, which matches $f(x)$.
    :::

<1>3. Inductive Step: Assume the statement holds for some integer $k \ge 0$, i.e., $f^{(k)}(x) = (2^k x + k 2^{k-1}) e^{2x}$. Then it holds for $k+1$.
    Proof:
    <2>1. Differentiating $f^{(k)}(x)$ using the product rule:
        $$f^{(k+1)}(x) = \frac{d}{dx}\left[(2^k x + k 2^{k-1}) e^{2x}\right] = \left(\frac{d}{dx}(2^k x + k 2^{k-1})\right) e^{2x} + (2^k x + k 2^{k-1}) \left(\frac{d}{dx} e^{2x}\right).$$
    <2>2. Compute the components:
        $$\frac{d}{dx}(2^k x + k 2^{k-1}) = 2^k, \qquad \frac{d}{dx} e^{2x} = 2 e^{2x}.$$
    <2>3. Combine and factor out $e^{2x}$:
        $$f^{(k+1)}(x) = 2^k e^{2x} + 2(2^k x + k 2^{k-1}) e^{2x} = \left(2 \cdot 2^k x + 2^k + 2 k 2^{k-1}\right) e^{2x}$$
        $$= \left(2^{k+1} x + 2^k(1 + k)\right) e^{2x} = \left(2^{k+1} x + (k+1) 2^{(k+1)-1}\right) e^{2x}.$$
    This matches the formula for $n = k+1$.

<1>4. Alternative derivation using Leibniz's Rule:
    Proof:
    <2>1. Leibniz's Rule states that $(u v)^{(n)} = \sum_{k=0}^n \binom{n}{k} u^{(n-k)} v^{(k)}$.
    <2>2. Let $u(x) = x$ and $v(x) = e^{2x}$.
        Then $u^{(0)}(x) = x$, $u^{(1)}(x) = 1$, and $u^{(j)}(x) = 0$ for all $j \ge 2$.
        Also $v^{(k)}(x) = 2^k e^{2x}$ for all $k \ge 0$.
    <2>3. The sum has only two non-zero terms ($k=n$ and $k=n-1$ for $u^{(0)}$ and $u^{(1)}$):
        $$f^{(n)}(x) = \binom{n}{0} x (2^n e^{2x}) + \binom{n}{1} (1) (2^{n-1} e^{2x}) = (2^n x + n 2^{n-1}) e^{2x}.$$

<1>5. Conclusion: $f^{(n)}(x) = (2^n x + n 2^{n-1}) e^{2x} = 2^{n-1}(2x + n)e^{2x}$ for all $n \ge 0$.
    ::: {.proof}
    Follows from <1>1 through <1>4. Q.E.D.
    :::
:::
