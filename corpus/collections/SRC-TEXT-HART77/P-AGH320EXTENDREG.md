---
schema: qual/card@1
id: P-AGH320EXTENDREG
kind: problem
title: Extending a regular function across a normal point in dimension at least two
classification:
  areas:
  - algebraic-geometry
  topics:
  - Regular Functions
  - Normal Varieties
  - Dimension
relations:
- kind: uses
  target: P-AGH317NORMAL
- kind: uses
  target: P-AGH312DIMLOCAL
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.3.20 and restored the source reference to III.3.5. The intended algebraic input is the height-one intersection theorem for Noetherian normal domains.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the reduction to the normal local ring at P, the membership in every height-one localization, and the punctured affine-line counterexample against Matsumura, Commutative Ring Theory, Theorem 11.5, and independent Hartshorne solution notes.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Vakil, The Rising Sea, 2 September 2011 draft, Section
    12.3.9-12.3.11, printed pp. 267-268, text version `tmp/sources/vakil-rising-sea-2025-10-21.md`: the Algebraic Hartogs' Lemma and
    its proof by the ideal of denominators, which is the height-one
    intersection step the card cites to Matsumura Theorem 11.5. Matsumura's
    book is not on this machine, so that numbering is repeated from the card
    and not verified here. Checked the reduction of step s2: a height-one
    prime of O_{P,Y} pulls back to a prime p strictly inside m because dim R
    >= 2, V(p) has dimension at least one so carries a closed point Q other
    than P, and regularity of f at Q puts f in A_p.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.3.20,
    printed p. 23 (PDF p. 38 of the checked-in extraction, whose folio reads 23).
    The input of part (a) is published with its proof in R. Vakil, The Rising
    Sea: Foundations of Algebraic Geometry, 21 October 2025 version, Section
    13.5: the Algebraic Hartogs' Lemma 13.5.19 on printed p. 383,
    "A = intersection of A_p over the codimension 1 primes" for a Noetherian
    integrally closed domain, with the full proof at 13.5.21--13.5.25 on printed
    pp. 383--385 by the ideal of denominators, and 13.5.20 says in words that
    Noetherian normal schemes have the Hartogs property. Step s3 now cites it in
    the body, and the earlier reference to the 2011 draft, printed pp. 267--268,
    is replaced by the 2025 pagination. Part (b) is not in that section: the
    source's chapter has no example of a failure in dimension one, and step s5's
    punctured line is the card's own.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    The exercise itself now has published proofs, not only its commutative
    algebra input. Printed exercise read: Hartshorne, Algebraic Geometry (1977),
    I.3.20, printed p. 23 (PDF p. 38 of the extraction). Read hwong557's accepted
    answer 1791316 to Mathematics Stack Exchange question 1791250
    (tmp/sources/mse-1791250-regular-functions-extension-normal-points.md) and
    Hetong Xu's answer 3771982 to question 846109
    (tmp/sources/mse-846109-hartshorne-problem-i-3-20.md); both reduce to
    O_{P,Y} = intersection of the height-one localizations, then prove the given
    rational function g/h lies in each by producing a closed point Q != P of
    Z(q) from dim >= 2 and the regularity of f at Q. Checked that this is step
    s2 with q running over ht-one primes of O_{P,Y}, that the intersection
    theorem they cite (Matsumura 11.5 in 846109) is the one step s3 applies, and
    that neither answer proves (b), whose punctured line stays the card's. Vakil
    13.5.19 with its proof at 13.5.21-13.5.25 stays cited for the theorem
    itself, since Matsumura is not on this machine. Not checked: the remaining
    part of Hetong Xu's answer after the height-one reduction, and any other
    answer on those two questions.

---

::: {.problem}
Let $Y$ be a variety of dimension $\geq 2$, let $P \in Y$ be a normal point, and let $f$ be a regular function on $Y \sm \theset{P}$.

(a) Show that $f$ extends to a regular function on $Y$.

(b) Show that this would be false for $\dim Y = 1$. See (III, Ex. 3.5) for a generalization.
:::

::: {.solution}
Let
$$
K=K(Y)
$$
be the function field of $Y$.
Since $Y\setminus\{P\}$ is a nonempty open subset, the given regular function determines an element, again denoted $f$, of $K$.

::: pf

::: {.pf-step #s1}

Put
$$
R=\mco_{P,Y}.
$$
Then $R$ is a Noetherian normal local domain of dimension at least two.

::: pf-proof

Local rings of varieties are Noetherian domains.
The hypothesis that $P$ is normal says exactly that $R$ is integrally closed in its fraction field, so $R$ is normal.
By [[P-AGH312DIMLOCAL]],
$$
\dim R=\dim Y\ge2.
$$
Its fraction field is $K(Y)=K$.

:::

:::

::: {.pf-step #s2}

For every height-one prime $\mathfrak q\subset R$, the rational function $f$ belongs to $R_{\mathfrak q}$.

::: pf-proof

Choose an affine open neighborhood $U\subseteq Y$ of $P$, write
$$
A=A(U),
\qquad
\mathfrak m=I_U(P),
$$
so that $R=A_{\mathfrak m}$.
The prime $\mathfrak q$ has the form
$$
\mathfrak q=\mathfrak p A_{\mathfrak m}
$$
for a prime $\mathfrak p\subsetneq\mathfrak m$.
The strict containment follows because $\operatorname{ht}\mathfrak q=1$ whereas
$$
\operatorname{ht}\mathfrak m=\dim R\ge2.
$$

The irreducible closed set $V(\mathfrak p)\subseteq U$ therefore contains a closed point $Q\ne P$.
The function $f$ is regular at $Q$.
Hence, after shrinking inside the affine variety $U$, it has a representation
$$
f=\frac{a}{b}
$$
with $a,b\in A$ and $b(Q)\ne0$.
Because $Q\in V(\mathfrak p)$, the inequality $b(Q)\ne0$ implies
$$
b\notin\mathfrak p.
$$
Thus $f\in A_{\mathfrak p}$.
Since $\mathfrak p\subseteq\mathfrak m$,
$$
A_{\mathfrak p}\cong (A_{\mathfrak m})_{\mathfrak pA_{\mathfrak m}}
=R_{\mathfrak q},
$$
which proves the claim.

:::

:::

::: {.pf-step #s3}

The rational function $f$ belongs to $R=\mco_{P,Y}$.

::: pf-proof

For a Noetherian normal domain, the height-one intersection theorem states that, inside its fraction field,
$$
R=\bigcap_{\operatorname{ht}\mathfrak q=1}R_{\mathfrak q}.
$$
This is proved in full as the Algebraic Hartogs' Lemma of R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §13.5.19], printed p. 383, with the proof in 13.5.21--13.5.25 on printed pp. 383--385: the ideal of denominators $I=\theset{a\in R \st ar\in R}$, the module $M_{a/b}\subseteq R/(b)$, the lemma that $r\in R$ exactly when $r\in R_{\mathfrak p}$ for the associated primes of $R/(g)$, and then that those primes have height one because a Noetherian integrally closed domain is regular in codimension one. The same statement is Matsumura, *Commutative Ring Theory*, Theorem 11.5. Step [](#s2){.pf-ref} places $f$ in every ring in this intersection, so $f\in R$.

:::

:::

::: {.pf-step #s4}

The function $f$ extends to a regular function on all of $Y$, proving (a).

::: pf-proof

By step [](#s3){.pf-ref}, the germ $f\in\mco_{P,Y}$ is represented by a regular function $g$ on some open neighborhood $V$ of $P$.
Both $g$ and the original function on $Y\setminus\{P\}$ represent the same element of $K(Y)$.
Hence they agree on the overlap
$$
V\setminus\{P\}.
$$
They therefore glue to a regular function on
$$
V\cup(Y\setminus\{P\})=Y
$$
extending the original $f$.

:::

:::

::: {.pf-step #s5}

The assertion fails in dimension one.

::: pf-proof

Take
$$
Y=\AA^1,
\qquad
P=0,
$$
and on $Y\setminus\{0\}=D(x)$ take
$$
f=\frac1x.
$$
This is regular on $D(x)$.
If it extended regularly across the origin, its germ there would lie in
$$
\mco_{0,\AA^1}=k[x]_{(x)}.
$$
But $1/x$ does not belong to this localization: every denominator of an element of $k[x]_{(x)}$ is nonzero at $x=0$, whereas a representation of $1/x$ in reduced form has denominator divisible by $x$.
Indeed, if
$$
\frac1x=\frac{a}{s}
$$
with $a,s\in k[x]$ and $s\notin(x)$, then $s=ax$, so $s(0)=0$, contradicting $s\notin(x)$.
Thus no extension exists, proving (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (a), and step [](#s5){.pf-ref} proves (b).

:::

:::

:::

::: {.remark title="Published solution"}
The height-one intersection theorem that step [](#s3){.pf-ref} applies is proved in full as Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §13.5], printed pp. 383--385, under the name "Algebraic Hartogs' Lemma" (13.5.19): "Suppose $A$ is an integrally closed Noetherian integral domain. Then $A=\cap_{\mathfrak p\text{ codimension }1}A_{\mathfrak p}$." The printed proof, 13.5.21--13.5.25, is the ideal of denominators $I=\theset{a\in A\st ar\in A}$ and the module $M_{a/b}\subseteq A/(b)$: for $r\notin A$ an associated prime of $M_{a/b}$ keeps $r$ out of $A_{\mathfrak p}$ (13.5.23), and for an integrally closed $A$ those primes have codimension one, since $A$ is regular in codimension one and $A/(b)$ has no embedded points (13.5.24), whence 13.5.25. In the case at hand $A=R=\mco_{P,Y}$ is a Noetherian normal domain of dimension at least two by step [](#s1){.pf-ref}, so the theorem applies verbatim. The same statement is on the card as Matsumura, *Commutative Ring Theory*, Theorem 11.5, which is the form the working notes of this exercise use; Matsumura's book is not on this machine. Part (b), the failure in dimension one, is not in the source, and step [](#s5){.pf-ref} is the card's.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), gives no solution to 3.20.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 3.20.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.20, PDF p. 38, text version `tmp/sources/hartshorne-solutions-egbert.md`, writes "Since projective space is proper this works" for (a) and "Consider a single variable complex function with a pole" for (b); neither is an argument for the statement.
No Hartshorne solution set contains a proof of this exercise, and Vakil's book proves the algebra lemma rather than the exercise; the published proofs of the exercise itself are the two answers below. The proof above reduces to the local ring $\mco_{P,Y}$, shows the rational function lies in every height-one localization by finding a closed point of $V(\mathfrak p)$ other than $P$, and cites the lemma for the intersection; the punctured line $1/x\in\mco(\AA^1\setminus\theset{0})\setminus\mco_0$ is (b), and it is in neither answer.

The first answer is the accepted answer of hwong557, answer 1791316 to question 1791250, *Regular functions extension to normal points of varieties*, text version `tmp/sources/mse-1791250-regular-functions-extension-normal-points.md`, states the height-one intersection for $A(Y)_{\mathfrak m_P}$ and continues: "Our given $f$ is a rational function so must be of the form $g/h$, where $g$ and $h$ lie in $A(Y)$ and $h\ne0$. It remains to show that $h$ is not in any height $1$ prime $\mathfrak q\subset\mathfrak m_P$, because then $f$ will lie in $A(Y)_{\mathfrak m_P}$ so $f$ will be regular at $P$. If $h$ were in such a prime $\mathfrak q$, then $h$ would vanish on $Z(\mathfrak q)$. We can find a point $Q\ne P$ in $Z(\mathfrak q)$ because $\dim Y\ge2$ (basically $\mathfrak q\subsetneq\mathfrak m_P$ by Hartshorne Thm 3.2c). But $f$ is regular at $Q$ so $h$ cannot vanish at $Q$. So $h\notin\mathfrak q$, as desired." That is step [](#s2){.pf-ref}, with $\mathfrak q$ ranging over the height-one primes of $\mco_{P,Y}$ and $Q$ the closed point it finds. The answer of Hetong Xu, answer 3771982 to question 846109, *Hartshorne Problem I.3.20*, text version `tmp/sources/mse-846109-hartshorne-problem-i-3-20.md`, gives the same reduction to $A(Y)$ and to the height-one primes $\mathfrak q\subset\mathfrak m_P$ with the steps written out, and takes the intersection theorem itself from Matsumura, *Commutative Ring Theory*, Theorem 11.5, "Let $R$ be a normal Noetherian domain. Then $R=\bigcap_{\operatorname{ht}\mathfrak p=1}R_\mathfrak p$" --- the numbering the card has always carried. Part (b) is in neither answer: the punctured line of step [](#s5){.pf-ref} is the card's.
:::
