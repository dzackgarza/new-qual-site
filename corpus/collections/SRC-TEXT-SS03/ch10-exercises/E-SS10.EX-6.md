---
schema: qual/card@1
id: E-SS10.EX-6
kind: exercise
title: "SS 10.6: Exponential square-root bounds for the partition function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
6. Show as a consequence of Exercise 5 that

$$
e ^ {c _ {1} n ^ {1 / 2}} \leq p (n) \leq e ^ {c _ {2} n ^ {1 / 2}}
$$

for two positive constants $c _ { 1 }$ and $c _ { 2 }$ .

[Hint: $\begin{array} { r } { F ( e ^ { - y } ) = \sum p ( n ) e ^ { - n y } \le C e ^ { c / y } } \end{array}$ as $y \to 0$ . So $p ( n ) e ^ { - n y } \leq c e ^ { c / y }$ . Take $y =$ $1 / n ^ { 1 / 2 }$ to get $p ( n ) \leq c ^ { \prime } e ^ { c ^ { \prime } n ^ { 1 / 2 } }$ . In the opposite direction

$$
\sum_ {n = 0} ^ {m} p (n) e ^ {- n y} \geq C (e ^ {c / y} - \sum_ {n = m + 1} ^ {\infty} e ^ {c n ^ {1 / 2}} e ^ {- n y}),
$$

and it sufices to take $y = A m ^ { - 1 / 2 }$ where A is a large constant, and use the fact that the sequence $p ( n )$ is increasing.]
::: solution
**Goal:** Produce $p(n)\asymp e^{\Theta(\sqrt n)}$ bounds.

<1>1. Upper bound:
    *Proof:*  
    The hint gives constants $C,c>0$ with
    $$F(e^{-y})=\sum_{n\ge0}p(n)e^{-ny}\le C e^{c/y}\qquad(y\to0^+).$$
    So for each $n$,
    $$p(n)e^{-ny}\le C e^{c/y},\qquad\text{hence }p(n)\le C e^{c/y+ny}.$$
    Set $y=n^{-1/2}$:
    $$p(n)\le C e^{c\sqrt n+\sqrt n}=e^{c_2\sqrt n}.$$

<1>2. Lower bound:
    *Proof:*  
    Use
    $$\sum_{k=0}^m p(k)e^{-ky}\ge
    C\!\left(e^{c/y}-\sum_{k=m+1}^\infty e^{c\sqrt k}e^{-ky}\right).$$
    For fixed large $A$, set $y=A/\sqrt m$.
    Since $p$ is increasing,
    $$\sum_{k=0}^m p(k)e^{-ky}\le p(m)\sum_{k=0}^m e^{-ky}\le p(m)\frac1{1-e^{-y}}.$$
    Also
    $$\sum_{k=m+1}^\infty e^{c\sqrt k}e^{-ky}
    \le \sum_{k=m+1}^\infty e^{-(A-c)/\sqrt m\,k}
    =O\!\left(e^{-\eta\sqrt m}\right)$$
    for $A>c$ and some $\eta>0$.
    Thus for large $m$,
    \[
    p(m)\frac1{1-e^{-y}}\ge C' e^{c_1\sqrt m}
    \]
    with $c_1>0$. Since $1-e^{-y}\asymp A/\sqrt m$, absorb the polynomial factor into
    the exponential constant:
    \[
    p(m)\ge e^{c_1'\sqrt m}.
    \]

<1>3. Conclusion:
    *Proof:*  
    Renaming constants gives
    $$e^{c_1\sqrt n}\le p(n)\le e^{c_2\sqrt n}$$
    for all large $n$, and finitely many remaining $n$ are absorbed by larger constants.
:::
