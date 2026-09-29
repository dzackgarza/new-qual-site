---
schema: qual/card@1
id: P-APAF11H
kind: problem
title: 'Intersections of ideals: elimination, varieties, radicals, and a Gröbner computation'
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $I$ and $J$ be ideals in $k[x_1,\ldots,x_n]$ where $k$ is a field.

(i) Prove $I\cap J=(tI+(1-t)J)\cap k[x_1,\ldots,x_n]$.

(ii) Prove that $V(I\cap J)=V(I)\cup V(J)$ where for any set $X\subseteq k[x_1,\ldots,x_n]$, $V(X)$ is the affine variety defined by $X$.

(iii) Prove that $\sqrt{I\cap J}=\sqrt{I}\cap\sqrt{J}$.

(iv) Let $I=\langle x^3y\rangle$ and $J=\langle xy^3+xy\rangle$ be ideals in $k[x,y]$.
Find a Gröbner basis for $I\cap J$ relative to lexicographic order where $x>y$.
:::

::: {.solution}
**Part (i).**

::: pf

::: {.pf-step #p1-s1}
($\subseteq$) If $f \in I \cap J$, then $f = tf + (1-t)f \in tI + (1-t)J$, and $f \in k[x_1,\ldots,x_n]$.

::: pf-proof
$f \in I$ gives $tf \in tI$, and $f \in J$ gives $(1-t)f \in (1-t)J$.
:::

:::

::: pf-step
($\supseteq$) If $f \in (tI + (1-t)J) \cap k[x_1,\ldots,x_n]$, then $f = tg + (1-t)h$ with $g \in I$, $h \in J$.

::: pf-proof
definition of $tI + (1-t)J$.
:::

:::

::: {.pf-step #p1-s3}
Setting $t = 0$ gives $f = h \in J$; setting $t = 1$ gives $f = g \in I$.

::: pf-proof
substitute $t = 0$ and $t = 1$ (valid since $f$ does not involve $t$).
:::

:::

::: {.pf-step #p1-s4}
Hence $f \in I \cap J$.

::: pf-proof
step [](#p1-s3){.pf-ref}.
:::

:::

::: pf-qed
(i).

step [](#p1-s1){.pf-ref} and step [](#p1-s4){.pf-ref}.
:::

:::

**Part (ii).**

::: pf

::: {.pf-step #p2-s1}
$V(I \cap J) \supseteq V(I) \cup V(J)$.

::: pf-proof
$I \cap J \subseteq I$ and $I \cap J \subseteq J$, so $V(I) \subseteq V(I \cap J)$ and $V(J) \subseteq V(I \cap J)$.
:::

:::

::: {.pf-step #p2-s2}
$V(I \cap J) \subseteq V(I) \cup V(J)$.

::: pf-proof

::: pf-step
Let $p \in V(I \cap J)$.

::: pf-proof
take a point vanishing on $I \cap J$.
:::

:::

::: {.pf-step #p2-s2-2}
If $p \notin V(I)$, then there is $f \in I$ with $f(p) \neq 0$.

::: pf-proof
definition of $V(I)$.
:::

:::

::: {.pf-step #p2-s2-3}
For any $g \in J$, $fg \in I \cap J$, so $(fg)(p) = f(p)g(p) = 0$; since $f(p) \neq 0$, $g(p) = 0$.

::: pf-proof
$fg \in I \cap J$ and $p \in V(I \cap J)$.
:::

:::

::: {.pf-step #p2-s2-4}
Hence $p \in V(J)$.

::: pf-proof
step [](#p2-s2-3){.pf-ref} shows every $g \in J$ vanishes at $p$.
:::

:::

::: pf-step
Therefore $p \in V(I) \cup V(J)$.

::: pf-proof
step [](#p2-s2-2){.pf-ref}, step [](#p2-s2-3){.pf-ref}, and step [](#p2-s2-4){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
(ii).

step [](#p2-s1){.pf-ref} and step [](#p2-s2){.pf-ref}.
:::

:::

**Part (iii).**

::: pf

::: {.pf-step #p3-s1}
$\sqrt{I \cap J} = \sqrt{I} \cap \sqrt{J}$.

::: pf-proof

::: pf-step
($\subseteq$) If $f \in \sqrt{I \cap J}$, then $f^m \in I \cap J$ for some $m$, so $f^m \in I$ and $f^m \in J$, hence $f \in \sqrt I$ and $f \in \sqrt J$.

::: pf-proof
definition of the radical.
:::

:::

::: pf-step
($\supseteq$) If $f \in \sqrt I \cap \sqrt J$, then $f^m \in I$ and $f^n \in J$ for some $m, n$, so $f^{m+n} \in I \cap J$, hence $f \in \sqrt{I \cap J}$.

::: pf-proof
definition of the radical.
:::

:::

:::

:::

::: pf-qed
(iii).

step [](#p3-s1){.pf-ref}.
:::

:::

**Part (iv).**

::: pf

::: pf-step
$I \cap J = \langle x^3 y^3 + x^3 y \rangle$.

::: pf-proof
by part (i), $I \cap J = (t\langle x^3 y\rangle + (1-t)\langle xy^3 + xy\rangle) \cap k[x,y]$; computing the elimination ideal (Gröbner basis with $t > x > y$ and intersecting with $k[x,y]$) gives the single generator $x^3 y^3 + x^3 y$.
:::

:::

::: {.pf-step #p4-s2}
A Gröbner basis for $I \cap J$ (lex, $x > y$) is $\{x^3 y^3 + x^3 y\}$.

::: pf-proof
a single polynomial is its own Gröbner basis.
:::

:::

::: pf-qed
(iv).

step [](#p4-s2){.pf-ref}.
:::

:::
:::
