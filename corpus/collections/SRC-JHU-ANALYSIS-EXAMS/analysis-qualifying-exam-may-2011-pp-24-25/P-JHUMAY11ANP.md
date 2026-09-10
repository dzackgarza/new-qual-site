---
schema: qual/card@1
id: P-JHUMAY11ANP
kind: problem
title: The quadratic Schwarz bound for a two-sheeted branched disk map
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Read all three parts of Fall 2010 problem 8 on PDF page 27; restored the unit disk and the holomorphic example w squared, which the transcription incorrectly conjugated."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Included the global two-point fiber condition as well as derivative conditions, proved local covering sufficiency, and checked the removable quotient and the equality case forcing g(w)=iw squared."
---

::: problem
Let $D=\{w\in\mathbb C:|w|<1\}$, and let $g:D\to D$
be a surjective holomorphic map with $g(0)=0$. Suppose
that $g$ is a two-sheeted branched covering, with its
only ramification point at $w=0$. An example is $g(w)=w^2$.

(a) Express the given conditions explicitly in terms of $g$ and its derivatives.

(b) Show that $| g ( w ) | \leq | w | ^ { 2 }$ for all $| w | < 1$

(c) Suppose that $g ( 1 / 2 ) = i / 4$ . What is the strongest statement about $g ( w )$ that follows from the assertion in (b)? Explain.
:::

::: solution
<1>1. Part (a): derivatives determine local multiplicity, while fiber cardinalities specify the two sheets.

::: proof
For a holomorphic map $g:D\to D$, the explicit conditions are
$$
g(0)=0,\qquad g'(0)=0,\qquad g''(0)\ne0,\qquad
g'(w)\ne0\quad(0<|w|<1),
$$
together with
$$
g^{-1}(0)=\{0\},\qquad
\#g^{-1}(z)=2\quad(z\in D\setminus\{0\}).
$$
The fibers over nonzero values consist of distinct points.
Equivalently, every value in $D$ has two preimages counted
with multiplicity, and the only multiple point of a fiber
is the double zero at zero. The fiber conditions include
surjectivity; derivative conditions alone would not specify
the number of sheets.

To verify the equivalence, a two-sheeted holomorphic
branched covering has local multiplicity two at its
ramification point and multiplicity one elsewhere.
The Taylor series translates these assertions into the
displayed derivative conditions. The double preimage over
zero uses both sheets, so there can be no other preimage
of zero; a nonbranch value has exactly two simple preimages.

Conversely, suppose the displayed conditions hold. At each
of the two preimages of a nonzero value, the holomorphic
inverse function theorem gives a local inverse [@SS03].
Choose disjoint inverse neighborhoods and intersect their
image neighborhoods. Every value of this intersection
already has its two preimages in these neighborhoods;
the fiber count excludes any others. Thus the intersection
is evenly covered by two sheets.

Near zero write $g(w)=w^2h(w)$, where $h$ is holomorphic
and $h(0)=g''(0)/2\ne0$. On a small disk, $h$ is nonzero
and has a holomorphic square root $s$ [@SS03]. The local
coordinate $v=ws(w)$ has nonzero derivative at zero and
puts $g$ in the form $v^2$. A sufficiently small punctured
target disk has both its preimages in this coordinate
neighborhood; the fiber count again excludes any others.
This gives precisely the required single quadratic branch.
:::

<1>2. Part (b): division by the double zero gives the bound.

::: proof
Since $g(0)=g'(0)=0$, the function
$H(w)=g(w)/w^2$ for $w\ne0$ extends holomorphically
across zero by the Taylor series, with $H(0)=g''(0)/2$.
For $0<r<1$, on $|w|=r$ one has
$|H(w)|=|g(w)|/r^2\leq r^{-2}$, because $g(D)\subset D$.
The maximum modulus principle therefore gives
$|H(w)|\leq r^{-2}$ throughout $|w|\leq r$ [@SS03].
For a fixed $w\in D$, let $r\uparrow1$ with $r>|w|$.
It follows that $|H(w)|\leq1$, and hence
$$
|g(w)|=|w|^2|H(w)|\leq|w|^2.
$$
This argument uses only the disk bound and the double
zero, not the stronger global covering hypotheses.
:::

<1>3. Part (c): the extra value determines the entire map.

::: proof
The assumed value gives $H(1/2)=(i/4)/(1/4)=i$.
Thus the holomorphic function $H$, bounded by one,
attains modulus one at an interior point. The maximum
modulus principle makes $H$ constant [@SS03], and that
value fixes the constant as $i$. Consequently
$$
\boxed{g(w)=iw^2\quad\text{for all }w\in D.}
$$
This function satisfies every hypothesis: it has only
the double zero at zero, nonzero derivative elsewhere,
and exactly two distinct disk preimages of each nonzero
disk value. It also has the prescribed value at $1/2$.
:::
:::
