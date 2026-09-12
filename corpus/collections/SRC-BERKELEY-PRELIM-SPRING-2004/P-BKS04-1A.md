---
schema: qual/card@1
id: P-BKS04-1A
kind: problem
title: UC Berkeley Spring 2004 prelim 1A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Consider a sequence of functions $f _ { n } \colon [ a , b ] \to \mathbb { R }$ with the property that for each $x \in [ a , b ]$ there is an open interval $I _ { x }$ containing x such that $( f _ { n } ) _ { n \geq 1 }$ converges uniformly in $I _ { x } \cap [ a , b ]$ Show that $( f _ { n } ) _ { n \geq 1 }$ converges uniformly in $[ a , b ]$
:::

::: {.solution}
For each $x \in [ a , b ]$ , the sequence $\left( f _ { n } \right)$ converges uniformly on $I _ { x }$ , and in particular converges pointwise at x. Let $f \colon [ a , b ]  \mathbb { R }$ be the pointwise limit of $\left( f _ { n } \right)$ . The compact set $[ a , b ]$ is covered by the collection of open intervals $I _ { x } ,$ , so there is a finite subcovering, say ${ \bar { [ } } a , b { \bar { ] } } \subset \bigcup _ { k = 1 } ^ { m } I _ { x _ { k } }$ . Given $\epsilon > 0$ , there exists $N _ { k }$ such that for $n \geq N _ { k }$ , the difference $\vert f _ { n } - f \vert$ is bounded by  on $I _ { x _ { k } }$ . Let $N : = \operatorname* { m a x } ( N _ { 1 } , \dots , N _ { m } )$ . Then for $n \geq N$ , the difference $\vert f _ { n } - f \vert$ is bounded by  on all of $[ a , b ]$ . Hence by definition, $\left( f _ { n } \right)$ converges to $f$ uniformly.
:::
