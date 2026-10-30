---
schema: qual/card@1
id: P-UWALG09-8
kind: problem
title: Ideal quotients and the Zariski closure of $\mcv(I)\setminus\mcv(J)$
classification:
  areas:
  - algebra
  topics:
  - Polynomial Ideals
  - Affine Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Checked against Problem 8 of the UW 2009 algebra qualifying exam. The extraction garbled the ideal operator and the closure bar; they were read as I(S) and the overline from the definitions they stand in.
- event: solution-written
  by: claude-opus-5.5
  date: 2026-10-31
---

::: {.problem}
Recall the following basic definitions and facts about ideals and varieties.
Let $k$ be a field and $n$ be a positive integer.

- If $S\subseteq k^n$, the ideal of $S$ is $\mci(S)\coloneqq\{f\in k[x_1,\ldots,x_n]\st f(s)=0\ \forall s\in S\}$. $\mci(S)$ is a radical ideal in $k[x_1,\ldots,x_n]$.

- If $I\subseteq k[x_1,\ldots,x_n]$ is an ideal, then the variety of $I$ in $k^n$ is $\mcv(I)\coloneqq\{s\in k^n\st f(s)=0\ \forall f\in I\}$.

- If $S\subseteq k^n$, then $\mcv(\mci(S))$ is the smallest variety containing $S$ and is called the Zariski closure of $S$, denoted $\overline S$.

- Hilbert's Nullstellensatz: if $k$ is algebraically closed and $I$ is an ideal in $k[x_1,\ldots,x_n]$, then $\mci(\mcv(I))=\sqrt I$, where $\sqrt I$ is the radical of $I$.

(a) If $I$ and $J$ are ideals in $k[x_1,\ldots,x_n]$, the ideal quotient of $I$ by $J$ is
$$
I:J=\{f\in k[x_1,\ldots,x_n]\st fg\in I\ \forall g\in J\}.
$$
You may use without proof the fact that $I:J$ is an ideal in $k[x_1,\ldots,x_n]$ containing $I$.
Compute $\generators{xz,yz}:\generators{z}$ in $k[x,y,z]$.

(b) Compute $\mcv(\generators{xz,yz})$, $\mcv(\generators{z})$ and $\mcv(\generators{xz,yz}:\generators{z})$.

(c) Let $I$ and $J$ be ideals in $k[x_1,\ldots,x_n]$.

(i) Prove that $\mcv(I:J)\supseteq\overline{\mcv(I)\setminus\mcv(J)}$.

(ii) If $k$ is algebraically closed and $I=\sqrt I$, then prove that $\mcv(I:J)=\overline{\mcv(I)\setminus\mcv(J)}$.
(Check this statement in the example from parts (a) and (b).)
:::

::: {.solution}

::: pf

::: pf-step

(a) $\generators{xz,yz}:\generators{z}=\boxed{\generators{x,y}}$.

::: pf-proof

Since $xz,yz\in\generators{xz,yz}$, the generators $x,y$ lie in the quotient, so $\generators{x,y}\subseteq\generators{xz,yz}:\generators{z}$.
Conversely, if $fz\in\generators{xz,yz}$, write $fz=axz+byz$ with $a,b\in k[x,y,z]$. Then $z(f-ax-by)=0$, and $k[x,y,z]$ is a domain, so $f=ax+by\in\generators{x,y}$.
An element $f$ lies in $\generators{xz,yz}:\generators{z}$ exactly when $fz\in\generators{xz,yz}$, because every element of $\generators z$ is a multiple of $z$.

:::

:::

::: {.pf-step #varieties}

(b) $\mcv(\generators{xz,yz})=\boxed{\{z=0\}\cup\{x=y=0\}}$, the union of the $xy$-plane and the $z$-axis; $\mcv(\generators{z})=\boxed{\{z=0\}}$; and $\mcv(\generators{xz,yz}:\generators{z})=\mcv(\generators{x,y})=\boxed{\{x=y=0\}}$, the $z$-axis.

::: pf-proof

A point satisfies $xz=yz=0$ exactly when $z=0$ or $x=y=0$. The other two sets are read off from their generators, using part (a) for the third.

:::

:::

::: {.pf-step #inclusion}

(c)(i) $\mcv(I:J)\supseteq\overline{\mcv(I)\setminus\mcv(J)}$.

::: pf-proof

Let $s\in\mcv(I)\setminus\mcv(J)$, and choose $g\in J$ with $g(s)\neq0$. For $f\in I:J$ we have $fg\in I$, so $f(s)g(s)=0$ and hence $f(s)=0$. Thus $\mcv(I)\setminus\mcv(J)\subseteq\mcv(I:J)$.
The right side is a variety, and the Zariski closure is the smallest variety containing the set, so the closure lies in $\mcv(I:J)$ as well.

:::

:::

::: {.pf-step #equality}

(c)(ii) If $k$ is algebraically closed and $I=\sqrt I$, then $\mcv(I:J)=\overline{\mcv(I)\setminus\mcv(J)}$.

::: pf-proof

Write $S=\mcv(I)\setminus\mcv(J)$. By step [](#inclusion){.pf-ref} it remains to show $\mcv(I:J)\subseteq\overline S=\mcv(\mci(S))$, and for this it suffices that $\mci(S)\subseteq I:J$, since $\mcv$ reverses inclusions.
Let $h\in\mci(S)$ and $g\in J$. The product $hg$ vanishes on $S$ because $h$ does, and on $\mcv(J)$ because $g$ does, so it vanishes on $\mcv(I)\subseteq S\cup\mcv(J)$.
By the Nullstellensatz, $hg\in\mci(\mcv(I))=\sqrt I=I$. Hence $h\in I:J$.

:::

:::

::: pf-step

(c)(ii) The example of parts (a) and (b) satisfies the equality when $k$ is algebraically closed.

::: pf-proof

The ideal $I=\generators{xz,yz}$ is radical: it equals $\generators z\cap\generators{x,y}$, an intersection of prime ideals. Indeed, if $f=zh$ lies in $\generators{x,y}$, then $h\in\generators{x,y}$ because this ideal is prime and $z\notin\generators{x,y}$, so $f\in z\generators{x,y}=\generators{xz,yz}$; the reverse inclusion is clear.
By step [](#varieties){.pf-ref}, $\mcv(I)\setminus\mcv(\generators z)$ is the $z$-axis minus the origin, $\{(0,0,t)\st t\neq0\}$.
A polynomial vanishing there has $f(0,0,t)=0$ for the infinitely many $t\neq0$ in $k$, so it vanishes on the whole $z$-axis. The closure is therefore the $z$-axis, which is $\mcv(I:\generators z)$ by step [](#varieties){.pf-ref}, as step [](#equality){.pf-ref} predicts.

:::

:::

:::

:::
