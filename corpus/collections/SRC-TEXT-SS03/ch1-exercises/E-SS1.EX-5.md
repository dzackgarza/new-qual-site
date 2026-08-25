---
schema: qual/card@1
id: E-SS1.EX-5
kind: exercise
title: "A set Ω is said to be pathwise connected if any two points in Ω can be joined by"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
---

::: exercise
5. A set Ω is said to be pathwise connected if any two points in Ω can be joined by a (piecewise-smooth) curve entirely contained in Ω. The purpose of this exercise is to prove that an open set Ω is pathwise connected if and only if Ω is connected.

(a) Suppose first that Ω is open and pathwise connected, and that it can be written as $\Omega = \Omega _ { 1 } \cup \Omega _ { 2 }$ where $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are disjoint non-empty open sets. Choose two points $w _ { 1 } \in \Omega _ { 1 }$ and $w _ { 2 } \in \Omega _ { 2 }$ and let $\gamma$ denote a curve in Ω joining $w _ { 1 }$ to $w _ { 2 }$ . Consider a parametrization $z : [ 0 , 1 ] \to \Omega$ of this curve with $z ( 0 ) = w _ { 1 }$ and $z ( 1 ) = w _ { 2 }$ , and let

$$

t ^ {*} = \sup _ {0 \leq t \leq 1} \{t: z (s) \in \Omega_ {1} \text { for   all } 0 \leq s <   t \}.

$$

Arrive at a contradiction by considering the point $z ( t ^ { * } )$

(b) Conversely, suppose that Ω is open and connected. Fix a point $w \in \Omega$ and let $\Omega _ { 1 } \subset \Omega$ denote the set of all points that can be joined to w by a curve contained in Ω. Also, let $\Omega _ { 2 } \subset \Omega$ denote the set of all points that cannot be joined to w by a curve in Ω. Prove that both $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are open, disjoint and their union is Ω. Finally, since $\Omega _ { 1 }$ is non-empty (why?) conclude that $\Omega = \Omega _ { 1 }$ as desired.

The proof actually shows that the regularity and type of curves we used to define pathwise connectedness can be relaxed without changing the equivalence between the two definitions when Ω is open. For instance, we may take all curves to be continuous, or simply polygonal lines.<sup>2</sup>
:::
