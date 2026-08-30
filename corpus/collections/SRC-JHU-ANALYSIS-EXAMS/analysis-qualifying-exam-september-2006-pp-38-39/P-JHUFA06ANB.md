---
schema: qual/card@1
id: P-JHUFA06ANB
kind: problem
title: "Hurwitz theorem for uniformly convergent holomorphic sequences with one zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz's Theorem
  - Normal Families
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

2. Let $f _ { n } : D \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions on the unit disk D such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in D$ . Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $D$

b) Can $f _ { 0 }$ have no zeros?
If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

::: {.solution}
<1>1. Part (a): $f_0$ has at most one zero in $D$:
<2>1. By the Weierstrass Convergence Theorem, the uniform limit $f_0$ of holomorphic functions on $D$ is holomorphic on $D$.
Since $f_0$ is assumed to be non-constant, its zeros in $D$ are isolated.
Proof: Weierstrass Convergence Theorem and identity theorem.
<2>2. By Hurwitz's Theorem, if $z_0 \in D$ is a zero of $f_0$ of multiplicity $m \ge 1$, there exists $r > 0$ such that the closed disk $\overline{B(z_0, r)} \subset D$ contains no other zeros of $f_0$, and for all sufficiently large $n$, $f_n$ has exactly $m$ zeros (counted with multiplicity) in $B(z_0, r)$.
Proof: Hurwitz's Theorem on zeros of holomorphic limits.
<2>3. If $f_0$ had two distinct zeros $a, b \in D$, we could choose disjoint disks $B(a, r_1) \cap B(b, r_2) = \emptyset$ in $D$.
For sufficiently large $n$, $f_n$ would have at least one zero in $B(a, r_1)$ and at least one zero in $B(b, r_2)$, meaning $f_n$ has at least two zeros in $D$, contradicting $|f_n^{-1}(0)| = 1$.
Proof: disjoint isolating disks.
<2>4. If $f_0$ had a zero $z_0 \in D$ of multiplicity $m \ge 2$, then for large $n$, $f_n$ would have $m \ge 2$ zeros in $B(z_0, r)$, again contradicting $|f_n^{-1}(0)| = 1$.
Therefore $f_0$ has at most one zero in $D$ (and if present, it must be a simple zero).
Proof: multiplicity count via Hurwitz's Theorem.

<1>2. Part (b): $f_0$ can have no zeros, and condition on $(c_n)$:
<2>1. $f_0$ can indeed have no zeros in $D$.
For example, let $f_n(z) = z - (1 - \frac{1}{n})$ on $D$.
Each $f_n$ has unique zero $c_n = 1 - \frac{1}{n} \in D$, and $f_n(z) \to f_0(z) = z - 1$ uniformly on $D$.
The limit function $f_0(z) = z - 1$ has no zeros in $D$ since $|z| < 1 \implies z \neq 1$.
Proof: explicit example.
<2>2. **Necessary and sufficient condition:** $f_0$ has no zeros in $D$ if and only if $\lim_{n \to \infty} |c_n| = 1$ (i.e. the sequence of zeros $(c_n)$ has no accumulation points in $D$).
Proof: statement of condition.
<2>3. **Proof ($\Rightarrow$):** Suppose $f_0$ has no zeros in $D$.
If $(c_n)$ had an accumulation point $c \in D$, there would exist a subsequence $c_{n_k} \to c \in D$.
By uniform convergence on compact sets:
\[
f_0(c) = \lim_{k \to \infty} f_{n_k}(c_{n_k}) = \lim_{k \to \infty} 0 = 0,
\]
which means $c \in D$ is a zero of $f_0$, a contradiction.
Thus $(c_n)$ cannot accumulate anywhere in $D$, so $|c_n| \to 1$.
Proof: sequential continuity and uniform convergence.
<2>4. **Proof ($\Leftarrow$):** Suppose $\lim_{n \to \infty} |c_n| = 1$.
If $f_0$ had a zero $z_0 \in D$, by Hurwitz's Theorem there is a disk $B(z_0, r) \subset D$ such that $f_n$ has a zero in $B(z_0, r)$ for all large $n$.
Since $c_n$ is the unique zero of $f_n$, this implies $c_n \in B(z_0, r)$ for all large $n$, so $|c_n| \le |z_0| + r < 1$, contradicting $|c_n| \to 1$.
Thus $f_0$ has no zeros in $D$.
Proof: Hurwitz's Theorem applied to isolating disks.

<1>3. Conclusion:
$f_0$ has at most one zero in $D$, and $f_0$ is zero-free if and only if $|c_n| \to 1$. Q.E.D.
Proof: <1>1 and <1>2.
:::
