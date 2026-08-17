---
schema: qual/card@1
id: P-JKYJU
kind: problem
title: "Let $U \\subset \\mathbb{C}$ be an open set containing the closure $\\overline{D}$ of a unit disk."
classification:
  areas:
  - real-analysis
  topics:
  - hurwitz
  - holomorphic-functions
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $U \subset \mathbb{C}$ be an open set containing the closure $\overline{D}$ of a unit disk.
If a sequence $\{f_n : U \to \mathbb{C}\}$ of holomorphic functions converges uniformly to $f$ on compact subsets of $U$, then show that there exists an integer $N$ such that $f$ and $f_n$ have the same number of zeros in $D$ for $n \ge N$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $U \supset \overline{D}$ be open, $f_n: U \to \CC$ holomorphic, $f_n \to f$ uniformly on compact subsets of $U$.
Show that if $f$ has no zeros on $\bd D$, then there is $N$ such that $f$ and $f_n$ have the same number of zeros in $D$ (counting multiplicity) for all $n \ge N$.

<1>1. $f$ is holomorphic on $U$ and has finitely many zeros in $\overline{D}$.
Proof: $f$ is the locally uniform limit of holomorphic functions, hence holomorphic; if $f \not\equiv 0$ its zeros in the compact set $\overline{D}$ are isolated, hence finite.
(The case $f \equiv 0$ is excluded by the boundary hypothesis.)

<1>2. $m := \min_{z \in \bd D}|f(z)| > 0$.
Proof: $f$ has no zeros on $\bd D$ by hypothesis, $\bd D$ is compact, and $|f|$ is continuous there.

<1>3. For all sufficiently large $n$, $|f_n(z) - f(z)| < m$ on $\bd D$.
Proof: $f_n \to f$ uniformly on the compact set $\bd D$ (which is compactly contained in $U$), so the sup-norm distance tends to $0 < m$.

<1>4. $f$ and $f_n$ have the same number of zeros in $D$ for $n \ge N$.
Proof: on $\bd D$, <1>2 and <1>3 give $|f_n - f| < |f|$; by Rouch\'e's theorem, $f_n$ and $f$ have the same number of zeros in $D$ counting multiplicity.

<1>5. Q.E.D. Proof: <1>1–<1>4 prove the claim (this is Hurwitz's theorem in the counting form).
The hypothesis that $f$ have no zeros on $\bd D$ is necessary: e.g. $f(z) = z - 1$ (zero at $z = 1 \in \bd D$) with $f_n(z) = z - 1 + \tfrac{1}{n}$ has $0$ zeros in $D$ while $f_n$ has $1$.
:::
