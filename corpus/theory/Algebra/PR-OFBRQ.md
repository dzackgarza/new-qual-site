---
schema: qual/card@1
id: PR-OFBRQ
kind: proposition
title: Quadratic extensions in characteristic not $2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Classification
relations: []
review: draft
---

::: {.proposition}
Let $F$ be a field with $\ch(F)\neq 2$ and let $E/F$ be a field extension with $[E:F]=2$.
Then $E/F$ is [[D-5JYEI|Galois]], and $E=F(\sqrt{a})$ for some $a\in F$ that is not a square in $F$.
For $F=\QQ$, $a$ can be taken to be a squarefree integer different from $1$.
:::

::: {.proof}
Choose $\alpha\in E\setminus F$; then $E=F(\alpha)$ and the minimal polynomial of $\alpha$ over $F$ is $x^2+bx+c$ with $b,c\in F$.
Since $2$ is invertible in $F$, put $\beta\coloneqq\alpha+b/2$ and $a\coloneqq b^2/4-c\in F$.
Then $\beta^2=a$, $\beta\notin F$, and $E=F(\beta)=F(\sqrt a)$, so $a$ is not a square in $F$.
The roots of $x^2-a$ are $\pm\beta\in E$, and $\beta\neq-\beta$ because $\beta\neq0$ and $\ch(F)\neq2$.
Thus $E$ is the splitting field of the separable polynomial $x^2-a$, so $E/F$ is Galois.
For $F=\QQ$, write $a=m^2 d/n^2$ with $m,n$ nonzero integers and $d$ a squarefree integer; then $\QQ(\sqrt a)=\QQ(\sqrt d)$, and $d\neq1$ because $a$ is not a square.
:::
