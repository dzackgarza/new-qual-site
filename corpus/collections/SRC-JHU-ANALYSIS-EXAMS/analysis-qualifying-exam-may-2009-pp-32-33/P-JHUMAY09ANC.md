---
schema: qual/card@1
id: P-JHUMAY09ANC
kind: problem
title: "Uniformly convergent holomorphic sequences with a single zero each"
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
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

3. Let $f _ { n } : U \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in U$ , and U is a connected open set.
   Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $U$

b) Can $f _ { 0 }$ have no zeros?
If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

::: solution
**Goal:** Use Hurwitz to relate zeros of $f_n$ to zeros of $f_0$.

<1>1. At most one zero of $f_0$:
    *Proof:*  
    Suppose $f_0$ had two distinct zeros $z_1\ne z_2$ in connected $U$.
    Since $f_n\to f_0$ uniformly on compacta and $f_0$ is nonconstant, Hurwitz gives:
    for every small disk around each $z_j$, $f_n$ has a zero in that disk for all large $n$.
    These zeros are eventually distinct for disjoint disks, so $f_n$ would have at least two zeros for
    large $n$, contradicting $f_n^{-1}(0)=\{c_n\}$.
    Hence $f_0$ has at most one zero.

<1>2. If $f_0$ has a zero, then $(c_n)$ accumulates inside $U$:
    *Proof:*  
    If $f_0(c_0)=0$, choose a small disk $D$ with $\overline D\subset U$ around $c_0$.
    By Hurwitz, for large $n$ each $f_n$ has a zero in $D$, so $c_n\in D$ for all large $n$.
    Since each such $D$ contains at most one zero, this shows $c_n\to c_0$ along a subsequence.

<1>3. If $(c_n)$ accumulates in $U$, then $f_0$ has a zero:
    *Proof:*  
    Let $c_{n_k}\to c_0\in U$. For any $\varepsilon>0$, pick $k$ large with
    $c_{n_k}\in B(c_0,\varepsilon)\subset U$ and then compact-uniform convergence gives
    $f_{n_k}(c_0)\to f_0(c_0)$.
    But $|f_{n_k}(c_{n_k})-f_{n_k}(c_0)|\to0$ by continuity and $c_{n_k}\to c_0$, while
    $f_{n_k}(c_{n_k})=0$, so $f_0(c_0)=0$.

<1>4. Criterion for no zero of $f_0$:
    *Proof:*  
    By <2> and <3>, $f_0$ has no zeros in $U$ exactly when $(c_n)$ has no convergent subsequence
    in $U$, i.e. no interior accumulation point.
:::
