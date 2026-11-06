---
schema: qual/card@1
id: P-UCTOP290-S6-6
kind: problem
title: Retractions, sections, and splitting of an exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 6 in its checked-in extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 6, problems 6 and 6(c)
    (assets/attachments/UCSD_290_F14_sheet6.pdf, printed pages 258 and 259),
    from the checked-in extraction and a 300 dpi render, which shows the
    commuting diagram of part (c) with id_A, theta and id_C as the vertical maps
    and A -> A + C -> C along the bottom. The printed parts (a), (b), (c) and the
    closing sentence about free C match the card. No repair was needed.
---

::: {.problem}
For a short exact sequence of abelian groups
$$
0\to A\xrightarrow{i}B\xrightarrow{p}C\to0,
$$
prove that the following are equivalent:
$i$ has a retraction, $p$ has a section, and
$B\cong A\oplus C$ compatibly with $i$ and $p$.
Show that the sequence splits if $C$ is free.
:::

::: {.solution}

Let $0\to A\xrightarrow{i}B\xrightarrow{p}C\to0$ be a short exact sequence of
abelian groups.

::: pf

::: {.pf-step #retract}

If there is a retraction $r\colon B\to A$ with $r\circ i=1_A$, then $p$ has a
section.

::: pf-proof

For $c\in C$ choose $b\in B$ with $p(b)=c$, possible by surjectivity of $p$,
and set $s(c)=b-i(r(b))$. If $b$ is replaced by $b+i(a)$, then $s$ becomes
$b+i(a)-i(r(b)+a)=b-i(r(b))$, using that $r\circ i$ is the identity; so $s(c)$
is independent of the choice. The formula $b\mapsto b-i(r(b))$ is a
homomorphism, hence so is $s$, and $p(s(c))=p(b)-p(i(r(b)))=c-0=c$ because
$\operatorname{im}i=\ker p$. So $s$ is a section.

:::

:::

::: {.pf-step #section}

If there is a section $s\colon C\to B$ with $p\circ s=1_C$, then $i$ has a
retraction.

::: pf-proof

For $b\in B$ the element $b-s(p(b))$ lies in $\ker p=\operatorname{im}i$, so
it is $i(a)$ for a unique $a\in A$, uniqueness because $i$ is injective; set
$r(b)=a$. The map $r$ is a homomorphism: $r(b+b')$ is determined by
$i(r(b+b'))=(b+b')-s(p(b)+p(b'))=i(r(b))+i(r(b'))=i(r(b)+r(b'))$ and
injectivity of $i$. Finally $r(i(a))$ is the unique $a'$ with
$i(a')=i(a)-s(p(i(a)))=i(a)$, so $r\circ i=1_A$.

:::

:::

::: {.pf-step #splits}

The sequence splits in the sense of part (c) if and only if either, hence
both, of the previous two conditions hold.

::: pf-proof

Given a section $s$, the map $\theta\colon A\oplus C\to B$,
$\theta(a,c)=i(a)+s(c)$, is a homomorphism and makes the diagram commute: its
composite with the inclusion of $A$ is $i$, and $p\theta(a,c)=0+c$. It is
injective, since $i(a)+s(c)=0$ gives $c=-p(s(c))=-p(i(a))=0$ and then $a=0$,
and it is surjective onto $B$, since $b=i(r(b))+s(p(b))$ using the retraction
built in step [](#section){.pf-ref}. Conversely an isomorphism $\theta$ making
the diagram commute gives a retraction $\theta^{-1}$ followed by the
projection to $A$, and a section of $p$ by $\theta$ on $C$.

:::

:::

::: {.pf-step #free}

If $C$ is free the sequence splits.

::: pf-proof

Choose a basis $\{e_\lambda\}$ of $C$ and, using surjectivity of $p$, an
element $b_\lambda\in B$ with $p(b_\lambda)=e_\lambda$ for each $\lambda$.
Since $C$ is free on those elements, there is a unique homomorphism $s\colon
C\to B$ with $s(e_\lambda)=b_\lambda$, and $p\circ s=1_C$ because the two
sides agree on the basis. So $p$ has a section and the sequence splits by step
[](#splits){.pf-ref}.

:::

:::

:::


:::
