---
schema: qual/card@1
id: P-JHUFA06ANB
kind: problem
title: "Hurwitz theorem for uniformly convergent holomorphic sequences with one zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz
  - Normal Families
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
2. Let $f _ { n } : D \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions on the unit disk D such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in D$ . Suppose that $f _ { n } \to f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $D$

b) Can $f _ { 0 }$ have no zeros?
If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.
:::

::: {.solution}
The uniform limit $f_0$ of holomorphic functions is holomorphic on $D$, and it is nonconstant, so its zeros are isolated.

::: pf

::: {.pf-step #s1}

(a) $f_0$ has at most one zero in $D$.

::: pf-proof

For a zero $z_0$ of $f_0$, take $r>0$ with $\overline{B(z_0,r)}\subset D$ containing no other zero of $f_0$. By Hurwitz's theorem, $f_n$ has a zero in $B(z_0,r)$ for all large $n$. If $f_0$ had two distinct zeros, disjoint such disks would give each large $f_n$ two distinct zeros, while $f_n^{-1}(0)=\{c_n\}$.

:::

:::

::: {.pf-step #s2}

The zero in step [](#s1){.pf-ref} may be multiple: $f_n(z)=\bigl(z-\frac1n\bigr)^2$ has $f_n^{-1}(0)=\{\frac1n\}$ and converges uniformly on $D$ to $z^2$.

::: pf-proof

$\abs{f_n(z)-z^2}=\abs{-\frac2nz+\frac1{n^2}}\le\frac3n$ on $D$.

:::

:::

::: {.pf-step #s3}

(b) Yes: $f_n(z)=z-\bigl(1-\frac1n\bigr)$ has the single zero $c_n=1-\frac1n$ and converges uniformly on $D$ to $z-1$, which has no zero in $D$.

::: pf-proof

$\abs{f_n(z)-(z-1)}=\frac1n$ for all $z$.

:::

:::

::: {.pf-step #s4}

(b) $f_0$ has no zero in $D$ if and only if $\boxed{\abs{c_n}\to1}$.

::: pf-proof

If $\abs{c_n}\not\to1$, a subsequence $c_{n_k}$ converges to some $c\in D$, and uniform convergence with continuity of $f_0$ gives $f_0(c)=\lim_kf_{n_k}(c_{n_k})=0$. Conversely, if $f_0(z_0)=0$ for some $z_0\in D$, Hurwitz's theorem gives, for $r$ as in step [](#s1){.pf-ref}, a zero of $f_n$ in $B(z_0,r)$ for all large $n$; that zero is $c_n$, so $\abs{c_n}\le\abs{z_0}+r<1$ for all large $n$, and $\abs{c_n}\not\to1$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} answer part (a), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} answer part (b).

:::

:::

:::
