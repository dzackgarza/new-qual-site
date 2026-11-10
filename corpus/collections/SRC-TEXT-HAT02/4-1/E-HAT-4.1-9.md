---
schema: qual/card@1
id: E-HAT-4.1-9
kind: problem
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 9 and the 2021-06-02 correction; corrected i^* to i_* in the stored statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct in its two parts. The extension by `pi_0(X,A,x_0) = pi_0(X,x_0) /
    i_* pi_0(A,x_0)` is exact at the tail because the components of `X` mapping to the distinguished
    relative class are precisely those meeting `A`, and the quotient map is onto. (a) The five-lemma in
    degrees `>= 2` is the ordinary one; in the pointed-set tail the argument is the appropriate
    replacement — exactness says that the fiber of the next map over the distinguished element is the
    image of the preceding map — and the hypothesis that the four surrounding maps are bijections *for all
    basepoints* is exactly what allows rebasing at an arbitrary component, which is the one place the
    naive group-theoretic version fails. (b) The triple sequence stops at `pi_0(A,B,x_0)` because there is
    no distinguished element of `pi_0(B)` to feed the next term. No correction was needed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The printed part (a) is not correct as stated, and the earlier note's claim that "the hypothesis
    that the four surrounding maps are bijections for all basepoints is exactly what allows rebasing"
    does not repair it: rebasing is not available, because the basepoint of the pair $(Y,B)$ must lie
    in $B$ while the component of $B$ whose surjectivity is in question need not meet the image of
    $A$. Counterexample on the card: $X$ the disjoint union of a point $x_0$ and a point $a$ with
    $A=\{x_0,a\}$, $Y$ the disjoint union of a point $y_0$ and the interval $[0,1]$ with
    $B=\{y_0,0,1\}$, and $\varphi(x_0)=y_0$, $\varphi(a)=0$. Then the vertical maps at
    $\pi_1(X,A,x_0)$, $\pi_1(X,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$ are all bijections of
    one-point or two-point sets, while $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is 2 points into 3 and is not
    onto. The card now states the exercise as printed and proves what is true: the five-lemma at
    every term in degrees $\ge1$ (both chases written out), the bijectivity of the vertical at
    $\pi_0(X,A,x_0)$ from those at $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$, and the surjectivity at
    $\pi_0(A,x_0)$ for the components of $B$ lying in the component of $y_0$ in $Y$. Part (b) is
    correct as printed and its example is checked point by point.
---

::: {.problem}
Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i_*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.
:::

::: {.solution}
Define, for a pointed pair $(X,A,x_0)$,
$$
\pi_0(X,A,x_0)=\pi_0(X,x_0)\big/\,i_*\pi_0(A,x_0),
$$
the quotient pointed set, so that every component of $X$ meeting $A$ becomes the distinguished element. Then
$$
\pi_0(A,x_0)\xrightarrow{i_*}\pi_0(X,x_0)\xrightarrow{j_*}\pi_0(X,A,x_0)\longrightarrow0
$$
is exact as a sequence of pointed sets: the components mapping to the distinguished relative class are exactly those meeting $A$, and $j_*$ is onto. Exactness of the whole extended sequence at every other term is Theorem 4.3 (p. 344).

Throughout, a map of pairs $\varphi:(X,A,x_0)\to(Y,B,y_0)$ induces a ladder between the two sequences, commutative by naturality of the long exact sequence (p. 345), and "exact" for pointed sets means that the image of one map is the fiber of the next over the distinguished element.

### (a) The five-lemma

*Degrees $\ge1$: the group case.* The standard five-lemma argument applies verbatim, since every term there is a group and every map a homomorphism. Write the ladder as
$$
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D\xrightarrow{k}E
\quad\text{over}\quad
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D'\xrightarrow{k'}E'
$$
with all four squares commutative and both rows exact.

- *Injectivity of $\gamma:C\to C'$*, given $\alpha$ onto and $\beta,\delta$ one-to-one: if $\gamma(c)=1$ then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ and $c=g(b)$ for some $b$. Then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto. Hence $\beta(b)=\beta f(a)$, so $b=f(a)$ by injectivity of $\beta$, and $c=g(b)=gf(a)=1$.
- *Surjectivity of $\gamma$*, given $\beta$ and $\delta$ onto and $\varepsilon$ one-to-one: for $c'\in C'$ put $d'=h'(c')$ and choose $d\in D$ with $\delta(d)=d'$. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(c)$ for some $c\in C$. Now $h'(\gamma(c))=\delta h(c)=d'=h'(c')$, so $h'(\gamma(c)^{-1}c')=1$ and therefore $\gamma(c)^{-1}c'=g'(b')$ for some $b'\in B'$; choose $b\in B$ with $\beta(b)=b'$ and put $c''=c\,g(b)$. Then $\gamma(c'')=\gamma(c)g'(b')=c'$.

So every interior vertical map of a window of five consecutive terms all of which are groups is a bijection when its four neighbours are. In the pair sequence these windows are those lying in degrees $\ge2$, together with the window $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)$ read only up to its middle term; the window whose middle term is the pointed set $\pi_1(X,A,x_0)$ and the windows in degrees $0$ are treated next.

*The low-degree tail.* The three last terms are the pointed sets $\pi_0(A,x_0)$, $\pi_0(X,x_0)$, $\pi_0(X,A,x_0)$, and here multiplication is not available, so the argument above does not apply. What does hold, and what the exercise's clause "for all choices of $x_0$" is for, is the following.

*Claim 1.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$ are bijections, then so is the vertical map at $\pi_0(X,A,x_0)$. Indeed that map is induced by a bijection $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ which carries the subset $i_*\pi_0(A,x_0)$ bijectively onto $i_*\pi_0(B,y_0)$, and a bijection of sets carrying one subset onto another induces a bijection of the quotients.

*Claim 2.* Let the vertical map at $\pi_1(X,A,x_0)$ be onto and the vertical map at $\pi_0(X,x_0)$ be a bijection. Then every component of $B$ that lies in the component of $y_0$ in $Y$ is the image of a component of $A$: such a component is $\partial'\xi$ for some $\xi\in\pi_1(Y,B,y_0)$, because exactness at $\pi_0(B,y_0)$ says the image of $\partial'$ is the fiber of $\pi_0(B,y_0)\to\pi_0(Y,y_0)$ over the distinguished element; lift $\xi$ to $\eta$, and then $\varphi(\partial\eta)=\partial'(\varphi_*\eta)=\partial'\xi$ by naturality of $\partial$.

*The printed statement fails at $\pi_0(A,x_0)$ without a further hypothesis.* Take $X$ the disjoint union of a point $x_0$ and a point $a$, and $A=\{x_0,a\}$; take $Y$ the disjoint union of a point $y_0$ and the interval $[0,1]$, and $B=\{y_0,0,1\}$; let $\varphi$ send $x_0\mapsto y_0$ and $a\mapsto 0$. Then $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ is a bijection of two-element sets, $\pi_0(X,A,x_0)$ and $\pi_0(Y,B,y_0)$ are both one-point sets (in each case $i_*\pi_0$ is everything), $\pi_1(X,A,x_0)$ and $\pi_1(Y,B,y_0)$ are both one-point sets (no path in $Y$ joins $[0,1]$ to $y_0$), and $\pi_1(X)\to\pi_1(Y)$ is a bijection of one-point sets. So all four surrounding maps are bijections, yet $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is the inclusion of a two-element set into a three-element set and is not onto: the component $\{1\}$ of $B$ is not hit. The conclusion of the exercise therefore holds at every term in degrees $\ge1$ and at the last term $\pi_0(X,A,x_0)$, and at $\pi_0(A,x_0)$ it holds for the components of $B$ that lie in the component of $y_0$ in $Y$ (Claim 2), which is the sense in which the five-lemma is available in the low degrees.

### (b) The triple sequence

For $B\subset A\subset X$ the triple sequence of Theorem 4.3 ends
$$
\cdots\longrightarrow\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,B,x_0),
$$
and it cannot in general be continued by $\pi_0(X,B,x_0)$. Take $X$ the disjoint union of a point $b_0$ and an interval, $x_0=b_0$, and $B=\{b_0,b_1\}$ with $b_1$ a point of the interval; let $A=\{b_0,b_1,a_1\}$ with $a_1\neq b_1$ a further point of the interval, so that $b_1$ and $a_1$ lie in different components of the subspace $A$ while lying in the same component of $X$. Then the class of $a_1$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ is not the distinguished element, because its component of $A$ does not meet $B$; but its image in $\pi_0(X,B,x_0)$ is distinguished, because every component of $X$ that meets $B$ is collapsed and $a_1$ lies in the component of $b_1$. On the other hand the class of $a_1$ is not in the image of $\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0)$, since a path in $X$ starting in $A$ and ending at $x_0=b_0$ stays in the component $\{b_0\}$ of $X$, so its starting point lies in the component $\{b_0\}$ of $A$, which is collapsed. Hence appending $\pi_0(X,B,x_0)$ would destroy exactness at $\pi_0(A,B,x_0)$.

With the sequence ending at $\pi_0(A,B,x_0)$, the five-lemma holds for the ladder of triple sequences up to that terminal term, with the same qualifications as in (a): the windows of group terms are covered by the group case, and the terminal term is a quotient of pointed sets, where the analogue of Claim 2 applies with $B$ in the role of the subgroup and $A$ in the role of the pair.
:::
