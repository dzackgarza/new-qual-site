---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-06
kind: problem
title: 'Failure of uniform convergence for $f(x^n)$ when endpoint values differ'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - convergence-of-functions
  - counterexamples
relations: []
review: draft
---

::: {.problem title="?"}
(June 2010 #6a) Let $f:[0,1]\to\mathbb R$ be continuous with $f(0)\ne f(1)$ and define $f_n(x)=f(x^n)$.
Prove that $f_n$ does not converge uniformly on $[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Show that $f_n(x) = f(x^n)$ does not converge uniformly on $[0,1]$ when $f$ is continuous with $f(0) \neq f(1)$.

<1>1. $f_n \to f(0)$ pointwise on $[0,1)$ and $f_n(1) = f(1)$ for all $n$.
    Proof: For $x \in [0,1)$, $x^n \to 0$, so $f_n(x) = f(x^n) \to f(0)$ by continuity of $f$ at $0$. At $x = 1$, $x^n = 1$, so $f_n(1) = f(1)$ exactly.

<1>2. The pointwise limit is the function $g(x) = f(0)$ on $[0,1)$ with $g(1) = f(1)$.
    Proof: by <1>1.

<1>3. The pointwise limit $g$ is discontinuous at $1$ (unless $f(0) = f(1)$).
    Proof: $\lim_{x \to 1^-} g(x) = f(0)$ while $g(1) = f(1)$; these differ by hypothesis.

<1>4. $f_n$ does not converge uniformly to any function on $[0,1]$.
    Proof: A uniform limit of continuous functions is continuous. Each $f_n$ is continuous (composition of continuous $f$ with the continuous $x \mapsto x^n$), so a uniform limit of the $f_n$ would be continuous. But the only possible limit is $g$ of <1>2 (limits are unique, and uniform convergence implies pointwise convergence), and $g$ is discontinuous by <1>3. Contradiction.

<1>5. Q.E.D.
    Proof: <1>4 is the claim.

:::
