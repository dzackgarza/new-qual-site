<!-- page 1 -->

# Math 131: Introduction to Topology ¹

Professor Denis Auroux

Fall, 2019

## Contents

|  9/4/2019 - Introduction, Metric Spaces, Basic Notions | 3  |
| --- | --- |
|  9/9/2019 - Topological Spaces, Bases | 9  |
|  9/11/2019 - Subspaces, Products, Continuity | 15  |
|  9/16/2019 - Continuity, Homeomorphisms, Limit Points | 21  |
|  9/18/2019 - Sequences, Limits, Products | 26  |
|  9/23/2019 - More Product Topologies, Connectedness | 32  |
|  9/25/2019 - Connectedness, Path Connectedness | 37  |
|  9/30/2019 - Compactness | 42  |
|  10/2/2019 - Compactness, Uncountability, Metric Spaces | 45  |
|  10/7/2019 - Compactness, Limit Points, Sequences | 49  |
|  10/9/2019 - Compactifications and Local Compactness | 53  |
|  10/16/2019 - Countability, Separability, and Normal Spaces | 57  |
|  10/21/2019 - Urysohn's Lemma and the Metrization Theorem | 61  |

¹ Please email Beckham Myers at bmyers@college.harvard.edu with any corrections, questions, or comments. Any mistakes or errors are mine.

<!-- page 2 -->

|  10/23/2019 - Category Theory, Paths, Homotopy | 64  |
| --- | --- |
|  10/28/2019 - The Fundamental Group(oid) | 70  |
|  10/30/2019 - Covering Spaces, Path Lifting | 75  |
|  11/4/2019 - Fundamental Group of the Circle, Quotients and Gluing | 80  |
|  11/6/2019 - The Brouwer Fixed Point Theorem | 85  |
|  11/11/2019 - Antipodes and the Borsuk-Ulam Theorem | 88  |
|  11/13/2019 - Deformation Retracts and Homotopy Equivalence | 91  |
|  11/18/2019 - Computing the Fundamental Group | 95  |
|  11/20/2019 - Equivalence of Covering Spaces and the Universal Cover | 99  |
|  11/25/2019 - Universal Covering Spaces, Free Groups | 104  |
|  12/2/2019 - Seifert-Van Kampen Theorem, Final Examples | 109  |

2

<!-- page 3 -->

## 9/4/2019 - Introduction, Metric Spaces, Basic Notions

The instructor for this course is Professor Denis Auroux. His email is auroux@math.harvard.edu and his office is SC539. He will be hosting office hours Monday 12:30-2 and Tuesday 9-10:30. The course website is http://math.harvard.edu/auroux/131f19/. All information will be posted on the course webpage, although we will use Canvas to record grades.

There will be homework due every week on Wednesday, along with a take-home midterm and an in class final. We will loosely follow Munkres' Topology. The only prerequisites are some familiarity with the notion of a group and some comfort with metric spaces/the ability to manipulate open and closed sets.

### Introduction

Broadly, geometry is the study of measuring quantities. Mathematicians then use these measurements to make conclusions about properties of the spaces being studied. Topology, on the other hand, studies spaces by asking questions from a qualitative perspective. For example, some topological questions include:

- Is a space connected?
- Is a space simply connected? This question provides a technique for distinguishing between a sphere and a torus. For on the torus, there exist closed curves which cannot be 'shrunk' to a point.
- Is a space oriented? For example, the regular cylinder is oriented (as it has two sides), while the Möbius space is not (it has only one side). Note that there are easier ways to distinguish these two, namely by examining their boundaries.

![img-0.jpeg](img-0.jpeg)

Algebraic topology is the field that studies invariants of topological spaces that measure these above properties. For example, the fundamental group measures how far a space is from being simply connected. Before this, however, we will develop the language of point set topology, which extends the theory to a much more abstract setting than simply metric spaces.

Today we will remain informal, but a topological space is an abstraction of metric spaces. In short, a topological space is a set equipped with the additional data necessary to make sense of what it means for points to be 'close' to each other. This will allow us to develop notions of limits and continuity.

3

<!-- page 4 -->

### The Power of Abstraction - Example from Analysis

We have the following classical theorem:

Theorem (The Extreme Value Theorem). Given a continuous function \( f:[a,b] \to \mathbb{R} \), \( f \) achieves is maximum and minimum in the interval \([a,b]\).

This theorem can be generalized to the following:

Theorem. Given a continuous function \( f: C \to \mathbb{R} \) from a compact set \( C \), \( f \) achieves its maximum and minimum in \( C \).

And this is itself a special case of an even more general theorem:

Theorem. Given a continuous function \( f: C \to X \) from a compact set \( C \) to a topological space \( X \), the image of \( f \) is compact.

This is one excellent example of the power of abstraction, as we can take existing results and expand them to vastly more generalize situations.

We will introduce metric spaces in order to motivate the definition of topological spaces (otherwise, the definition seems a bit arbitrary).

### Metric spaces and open sets

Definition. A metric space is a pair \((X,d)\), where \(X\) is a set and \(d:X\times X\to \mathbb{R}_{\geq 0}\) is the distance function. \(d\) should satisfy

1. \(d(x,x) = 0\) and \(d(x,y) > 0\) when \(x\neq y\), for all \(x,y\in X\).

2. \(d(x,y) = d(y,x)\), namely \(d\) is symmetric.

3.  \( d(x,z) \leq d(x,y) + d(y,z) \)  for all  \( x,y,z \in X \) . This is the triangle inequality, which says that the shortest path between two points is the ‘straight line’ between them.

### Examples

- The vector space \(\mathbb{R}^n\) with the Euclidean distance

\[
d (x, y) = \sqrt {\sum_ {i = 0} ^ {n} (y _ {i} - x _ {i}) ^ {2}}
\]

where \( x = (x_{1},\ldots ,x_{n}),y = (y_{1},\ldots ,y_{n})\in \mathbb{R}^{n} \), is a metric space. This is the usual distance in space. It's easy to check that this indeed defines a metric on the space \( \mathbb{R}^n \).

- Let \( Y \subset \mathbb{R}^n \). Then \( Y \) becomes a metric space under the induced metric. In particular, we define a metric on \( Y \) by simply restricting the metric \( d|_{Y \times Y} \) on \( X \).

4

<!-- page 5 -->

Note that this is not always the appropriate metric to use on a subspace. For example, the surface of the earth is a subset of space, but we don't usually measure the distance between two points on the earth by simply drawing a straight line between them in space.

- We can define another metric on $\mathbb{R}^n$ by taking

$$d_\infty(x, y) = \max_i |y_i - x_i|$$

You will check this a metric on the first homework.

- We can define another metric on $\mathbb{R}^n$ by taking

$$d_1(x, y) = \sum_{i=1}^n |y_i - x_i|$$

Once we have a notion of distance, we can discuss open sets. The idea of topological spaces will be to bypass the notion of distance and simply consider these open sets.

**Definition.** Given a metric space $(X, d)$ and a point $p \in X$, the **open ball** of radius $r \in \mathbb{R}_{>0}$ around $p$ is

$$B_r(p) = \{q \in X : d(p, q) < r\}$$

Such an open ball is sometimes referred to as the **open neighborhood** of $p$ of radius $r$.

Open balls are instances of *open sets*.

**Definition.** A subset $U \subset X$ is **open** if, for every point $x \in U$, there exists $\epsilon > 0$ such that $B_\epsilon(x) \subset U$.

![img-1.jpeg](img-1.jpeg)

The idea is that, in a open set, there exists a 'safety margin' around every point. Given a point $p$, one can move around in the set a certain distance and remain in the sense.

Some basic properties of open sets are

1. Open balls are open. This is a basic consequence of the triangle inequality. It is on the first homework.

5

<!-- page 6 -->

2. $\varnothing$ is open (vacuously).
3. $X$ is open (as all open balls are contained in $X$).
4. The arbitrary union of open sets is open (even infinitely many). This follows easily from the definition.
5. The intersection of finitely many open sets is open.

It is important to note that we can only expect that the intersection of finitely many open sets is still open. For example, open intervals are open in $\mathbb{R}$, but the intersection

$$\bigcap_{n \in \mathbb{N}} \left( -\frac{1}{n}, \frac{1}{n} \right) = \{0\}$$

is not open (as there are no open balls around 0 contained in $\{0\}$).

# Limits and closed sets

One very important notion in the theory of metric spaces is that of a sequence. Let $(X, d)$ be a metric space.

Definition. A sequence $p_1, p_2, \ldots \in X$ converges to a limit $p \in X$ if, for all $\epsilon > 0$, there exists some $N \in \mathbb{N}$ such that for all $n \geq N$ we have $d(p_n, p) < \epsilon$.

Lemma. If a sequence in a metric space converges to a limit, this limit is unique.

This is false in a general topological space. We will discuss the properties of a topological space that will guarantee a sequence has a unique limit.

We can formulate the notion of the convergence of a sequence without mentioning the limit point. In this case, we want that the points of a sequence become arbitrarily close to each other (whereas above, we demanded that the points become arbitrarily close to a given point $p$).

Definition. A sequence $p_1, p_2, \ldots \in X$ is Cauchy if, for all $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that for all $n, m \geq N$ we have $d(p_n, p_m) < \epsilon$.

It is easy to prove that a converging sequence is Cauchy using the triangle inequality. The idea is that, if all the points are becoming arbitrarily close to a given point $p$, then they are also becoming close to each other. The converse is not always true, however.

Definition. A metric space is complete if every Cauchy sequence also converges to a point.

In fact, every metric space $X$ is sitting inside a larger, complete metric space $\overline{X}$.

Remark. Given a metric space $X$, one can construct the completion of a metric space by considering the space of all Cauchy sequences in $X$ up to an appropriate equivalence relation. Then this space of Cauchy sequences is itself a metric space which restricts to the original metric space $X$.

Definition. A set $Z \subset X$ is closed if the complement $X \setminus Z$ is open.

6

<!-- page 7 -->

**Remark.** *A subset does not need to be open or closed. Subsets can be open, closed, open and closed, or neither open nor closed.*

For example, $\varnothing$ and $X$ are always both open and closed. We also have an alternative definition of closedness that applies in particular to metric spaces (whereas the above definition is the same for topological spaces).

**Proposition.** *In a metric space $X$, a subset $Z \subset X$ is **closed** if and only if for every sequence $p_1, p_2, \ldots \in Z$ that converges to a point $p \in X$, we have $p \in Z$.*

So in a metric space, these two definitions are equivalent. In a topological space, the second definition does not necessarily imply the first.

*Proof.* We will prove the forward implication by contradiction. Suppose there exists a sequence $\{p_n : n \in \mathbb{N}\}$ with $p_n \in Z$ that converges to a point $p \in X \setminus Z$. Then for all $r > 0$, there exists $N \in \mathbb{N}$ such that for all $n \geq N$, $d(p_n, p) < r$. Thus $B_r(p) \cap Z \neq \varnothing$ for all $r > 0$, and $B_r(p) \not\subset X \setminus Z$, which means that $X \setminus Z$ is not open, and hence $Z$ is not closed.

Conversely, suppose for contradiction that $Z$ is not closed. Then $X \setminus Z$ is not open, so take $p \in X \setminus Z$ such that $B_r(p) \cap Z \neq \varnothing$ for all $r > 0$. For each $n \in \mathbb{N}$, let $p_n \in B_{1/n}(p) \cap Z$. Then the sequence $p_1, p_2, \ldots$ converges to $p \in X \setminus Z$. $\square$

## Continuity

We'll now introduce the notion of continuity for maps between metric spaces.

**Definition.** *A function $f : X \to Y$ between metric spaces $(X, d_X)$ and $(Y, d_Y)$ is **continuous** if for all $x \in X$ and all $\epsilon > 0$, there exists $\delta > 0$ such that for all $p \in X$ with $d(p, x) < \delta$, we have $d(f(p), f(x)) < \epsilon$. In other words, we have*

$$f(B_\delta(x)) \subset B_\epsilon(f(x))$$

The idea is that, as points in the domain $X$ become close together, their images under $f$ become close together as well. There is in fact another characterization of continuity that doesn't involve as many quantifiers. This is how we will ultimately characterize continuity in arbitrary topological spaces.

**Theorem.** *A function $f : X \to Y$ is continuous if and only if for all open sets $U \subset Y$, the preimage $f^{-1}(U) \subset X$ is open.*

*Proof.* Assume that $f : X \to Y$ is continuous. Let $U \subset Y$ be an open set. We want to show $f^{-1}(U)$ is open, so let $p \in f^{-1}(U)$. Since $U$ is open and $f(p) \in U$, we can take $\epsilon > 0$ small enough so that $B_\epsilon(f(p)) \subset U$. By continuity, there exists $\delta > 0$ such that $f(B_\delta(p)) \subset B_\epsilon(f(p)) \subset U$, which means $B_\delta(p) \subset f^{-1}(U)$. Hence $f^{-1}(U)$ is open.

7

<!-- page 8 -->

Conversely, assume for all open $U \subset Y$ we have that $f^{-1}(U)$ is open. We want to show $f$ is continuous. Let $p \in X$ and let $\epsilon > 0$. The set $B_{\epsilon}(f(p))$ is open, so $f^{-1}(B_{\epsilon}(f(p)))$ is open and contains $p$. Then by definition of an open set, there exists a radius $\delta > 0$ such that $B_{\delta}(p) \subset f^{-1}(B_{\epsilon}(f(p)))$. This implies $f(B_{\delta}(p)) \subset B_{\epsilon}(f(p))$, so $f$ is continuous as desired.

This lays the groundwork for defining a topological space, which is a space in which one can extend all of these ideas of open/closed sets, limits and continuity without a distance function.

**Definition.** A topology $\mathcal{T}$ on a set $X$ is a set of subsets of $X$ (which are the open sets) that satisfy

1. $\varnothing, X \in \mathcal{T}$.
2. Arbitrary unions of elements of $\mathcal{T}$ are in $\mathcal{T}$.
3. Finite intersections of elements of $\mathcal{T}$ are in $\mathcal{T}$.

Note that these are exactly the properties we noted above for metric spaces. Next time we will give many examples of spaces that illustrate how pathological these can become.

One reason why we consider such an abstract definition is because there are topological spaces which are not metric spaces. For example, the space of continuous functions from $[a, b]$ to $\mathbb{R}$ can be given a topology that does not arise from a metric.

8

<!-- page 9 -->

# 9/9/2019 - Topological Spaces, Bases

Today we will begin to discuss topological spaces.²

Definition. A topological space is a set X with a topology T. A topology is a collection T ⊂ P(X).³ These are the open sets of X. T must satisfy

1. ∅, X ∈ T
2. If Uᵢ ∈ T for i ∈ I, then ⋃ᵢ Uᵢ ∈ T (arbitrary unions of open sets are open)
3. If U₁, …, Uₙ ∈ T, then U₁ ∩ … ∩ Uₙ ∈ T (finite intersections of open sets are open)

This definition formalizes the properties we saw for metric spaces and generalizes the notion of being open in the abstract. As before, we define the following.

Definition. A subset Z ⊂ X is closed if X \ Z is open.

It is easy to prove the following proposition with basic set theory.

Proposition. We have

1. ∅, X are closed
2. Arbitrary intersections of closed sets are closed
3. Finite unions of closed sets are closed

We will see that such spaces can be in fact quite pathological, but we will first start with some basic examples.

### Basic Examples

- Let (X, d) be a metric space. Then the set

$$\mathcal{T} = \{U \subset X : \text{for all } x \in U \text{ there exists } r > 0 \text{ such that } B_r(x) \subset U\}$$

defines a topology on X.

- Let X = {a, b}. A topology T must contain ∅ and X. It may or may not contain {a} or {b}. If they are both in T, this means that the two points are distinct and separate. If neither of them are in T, then the points are as close together as they could be (topologically indistinguishable). Finally, one could even declare {a} to be open and not {b}.
- Let X = {a, b, c}. We begin to see the conditions that the axioms place on valid topologies. For example, if {a} and {b} are open then {a, b} must be open. The possible

²Munkres, sections 12-13.

³P(X) is the power set P(X) = {A ⊂ X}.

9

<!-- page 10 -->

topologies range from $\mathcal{T} = \{\varnothing, X\}$ (the coarsest topology) to $\mathcal{T} = \mathcal{P}(X)$ (the finest topology).

Definition. The discrete topology on a set $X$ is given by $\mathcal{T} = \mathcal{P}(X)$.

In the discrete topology, every subset is both open and closed.

Definition. We say a topology $\mathcal{T}'$ is finer than $\mathcal{T}$ if it contains more open sets than $\mathcal{T}$, namely $\mathcal{T} \subset \mathcal{T}'$. We say $\mathcal{T}'$ is coarser then $\mathcal{T}$ if $\mathcal{T}' \subset \mathcal{T}$.

We use the terms fine and coarse because a finer topology distinguishes more between points. A finer topology also places more conditions on convergence. For example, a sequence in a topological space equipped with the discrete topology $\mathcal{T} = \mathcal{P}(X)$ converges if and only if it becomes constant at some point.

Note that two topologies need not be comparable. Sometimes neither one is a subset of the other. We can also consider more interesting examples.

### The Cofinite Topology

- Let $X$ be an infinite set and take

$$\mathcal{T} = \{S \subset X : X \setminus S \text{ is finite or } S = \varnothing\}$$

This is the finite complement topology, also called the cofinite topology. Although it seems contrived, when this topology is placed on a field it has a special place in algebraic geometry.

$\mathcal{T}$ is a topology. It contains $\varnothing, X$ by definition (in particular, it contains $\varnothing$ because of the additional condition we included). If $S = \bigcup_i U_i$ for $U_i \in \mathcal{S}$, either $S = \varnothing$ or $U_i \subset S$ where $U_i$ has finite complement. Then

$$X \setminus S \subset X \setminus U_i$$

So $X \setminus S$ is finite, and $S \in \mathcal{T}$. If we let $U_1, \ldots, U_n$ be open, then

$$X \setminus (\bigcap_{i=1}^n U_i) = \bigcup_{i=1}^n X \setminus U_i$$

which is the finite union of finitely many points, and hence finite. Thus $\bigcap_{i=1}^n \in \mathcal{T}$. So this is indeed a topology.

### Counterexample

- Let $X$ be an infinite set and take

$$\mathcal{T} = \{S \subset X : S \text{ finite or } S = X\}$$

$\mathcal{T}$ is not a topology, even though $\varnothing, X \in \mathcal{T}$. Any infinite proper subset $Y \subsetneq X$ can be

10

<!-- page 11 -->

written as the union

$$Y = \bigcup_{y \in Y} \{y\}$$

Each $\{y\}$ is in $\mathcal{T}$, but their union $Y$ is not contained in $\mathcal{T}$.

In these simple examples, we can afford to keep track of the open sets of a topology. But this is in general too much information for a space. For example, we don't keep in mind all of the open sets in $\mathbb{R}^n$ we working with its topology. In practice, it suffices to only consider a smaller subset of the open sets called a basis, which generates the topology.$^4$

**Definition.** A **basis** is a collection of subsets $\mathcal{B} \subset \mathcal{P}(X)$ such that

1. $\mathcal{B}$ covers $X$, namely $\bigcup_{B \in \mathcal{B}} B = X$.
2. If $B_1, B_2 \in \mathcal{B}$ and $x \in B_1 \cap B_2$, then there exists $B_3 \in \mathcal{B}$ such that $x \in B_3 \subset B_1 \cap B_2$

![img-2.jpeg](img-2.jpeg)

A basis is not usually a topology, but we can generate a topology from a basis.

**Definition.** The topology $\mathcal{T}$ generated by a basis $\mathcal{B}$ is defined as follows. $U \in \mathcal{T}$ if and only if for all $x \in U$, there exists $B \in \mathcal{B}$ such that $x \in B \subset U$.

This is analogous to a definition of what it means for a set to be open in a metric space. We can now interpret the second condition in the definition of a basis as saying that the intersection of two basis elements is open.

**Proposition.** The topology generated by a basis $\mathcal{B}$ is indeed a topology.

Proof. $\varnothing \in \mathcal{T}$ vacuously. Similarly, $X \in \mathcal{T}$ because of condition 1 above.

Let $U_i \in \mathcal{T}$. If $x \in \bigcup_i U_i$, then there exists $i$ such that $x \in U_i$. Since $U_i$ is open, there exists a basis element $B \in \mathcal{B}$ with

$$x \in B \subset U_i \subset \bigcup_i U_i$$

$^4$Despite the name, a topological basis is not very similar to the basis of a vector space. For example, the entire topology is a basis for itself. There is no notion of independence.

11

<!-- page 12 -->

Therefore arbitrary unions of open sets are open.

We will show finite intersections of open sets is open by showing $U_1 \cap U_2$ is open (as we can get to finite intersections by successively taking intersections of two open sets). Let $x \in U_1 \cap U_2$. Since both of these sets are open, there exist $B_1, B_2 \in \mathcal{B}$ with $x \in B_1 \subset U_1$ and $x \in B_2 \subset U_2$. By condition 2, there exists a basis element $B_3 \in \mathcal{B}$ with $x \in B_3 \subset B_1 \cap B_2 \subset U_1 \cap U_2$. Therefore finite intersections of open sets is open, and $\mathcal{T}$ is indeed a topology.

### Example

- Let $\mathcal{B} = \{B_r(x) : x \in \mathbb{R}^n, r > 0\}$. Then $\mathcal{B}$ is a basis for the usual metric topology on $\mathbb{R}^n$. $\mathcal{B}$ clearly covers all of $\mathbb{R}^n$ and satisfies condition 2 in the definition above.

However, we can define another basis for $\mathbb{R}^n$ as well given by the sets of open rectangles

$$(a_1, b_1) \times (a_2, b_2) \times \dots \times (a_n, b_n) = \{(x_1, x_2, \dots, x_n) : a_i < x_i < b_i \text{ for all } i\}$$

It is easy to check that this is indeed a basis.

Furthermore, this basis also generates the standard metric topology on $\mathbb{R}^n$, illustrating the important idea that there are many bases that generate a single topology. We will prove using tools developed below. In short, the idea will be that open rectangles are open in the metric ball sense. Similarly, open balls are open in the open-rectangle sense.

Right now, we don't have a very concrete description of the topology generated by a basis $\mathcal{B}$. The following proposition gives a more explicit way to understand open sets.

**Proposition.** Let $\mathcal{B}$ be a basis. The topology $\mathcal{T}$ generated by $\mathcal{B}$ is given by

$$\mathcal{T} = \left\{ \bigcup_i U_i : U_i \in \mathcal{B} \right\}$$

In words, the open sets of $\mathcal{T}$ are all unions of sets in $\mathcal{B}$.

Proof. If $U \in \mathcal{T}$, for all $x \in U$ there exists $B_x \in \mathcal{B}$ such that $x \in B \subset U$. Then

$$\bigcup_{\substack{B \in \mathcal{B} \\ B \subset U}} B = U$$

We have $\bigcup_{B \subset U} \subset U$ by definition. For any point $x \in U$, the set $B_x$ contains $x$ and is contained in $U$. Hence $U \subset \bigcup_{B \subset U} B$, so we have equality.

**Remark.** $\mathcal{T}$ is the smallest collection of subsets of $X$ that contains $\mathcal{B}$ and is a topology.

It is in this sense that a basis generates a topology. However, it is important to note that a basis, as well as the way to write an open set as the union of basis elements, is far from unique.

12

<!-- page 13 -->

### Examples

- There is a basis for the usual topology on \(\mathbb{R}\) given by all open intervals of the form \((a,b)\), where \(a < b\) and \(a, b \in \mathbb{R}\). Then the proposition says that every open subset of \(\mathbb{R}\) is the union of intervals. This union may not even be finite. For example, the set \(\mathbb{R} \setminus \mathbb{Z}\) is open, as it is the union

\[
\mathbb {R} \setminus \mathbb {Z} = \bigcup_ {n \in \mathbb {Z}} (n, n + 1)
\]

- Consider the complement of the Cantor set, given by

\[
X = \{x \in (0, 1): \text {   at   least   one   1   appears   in   the   base   3   expansion   of   } x \}
\]

![img-3.jpeg](img-3.jpeg)

There is no linear ordering of the countably many open intervals that appear in the union for \( X \).

- There is no open set in \(\mathbb{R}\) that requires uncountably many disjoint open intervals to write as a union. This is because every open interval contains a rational (in fact infinitely may rationals), and if there were uncountably many disjoint open intervals, there would be uncountably many rationals.

- The lower limit topology on \(\mathbb{R}\) is the topology \(\mathcal{T}_{\ell}\) generated by the basis

\[
\mathcal {B} = \{[ a, b): a <   b \text {   and   } a, b \in \mathbb {R} \}
\]

These sets cover \(\mathbb{R}\) and satisfy the intersection condition (in fact the nonempty intersection of two such half-open intervals is again a half-open interval). So \(\mathcal{B}\) is a basis.

\(\mathcal{T}_{\ell}\) is distinct from the usual topology \(\mathcal{T}\) on \(\mathbb{R}\), as \([a,b)\in \mathcal{T}_{\ell}\) but \([a,b)\notin \mathcal{T}\). However, \((a,b)\in \mathcal{T}_{\ell}\). This is because for all \(x\in (a,b)\), we have \(x\in [x,b)\subset (a,b)\). Therefore \(\mathcal{T}\subsetneq \mathcal{T}_{\ell}\), namely \(\mathcal{T}_{\ell}\) is finer than \(\mathcal{T}\) (or \(\mathcal{T}\) is coarser than \(\mathcal{T}_{\ell}\)).

Lemma. Let \(\mathcal{B},\mathcal{B}'\) be bases for topologies \(\mathcal{T},\mathcal{T}'\), respectively. Then \(\mathcal{T}'\) is finer than \(\mathcal{T}\) (meaning \(\mathcal{T} \subset \mathcal{T}'\)) if and only if \(\mathcal{B} \subset \mathcal{T}'\). Equivalently, \(\mathcal{T} \subset \mathcal{T}'\) if and only if for all \(B \in \mathcal{B}\) and \(x \in B\), there exists \(B' \in \mathcal{B}'\) such that \(x \in B' \subset B\).

This provides a way to compare topologies. Namely, to show one topology is finer than another we must find such basis elements.

13

<!-- page 14 -->

### The French train distance

- The *French train distance* on $\mathbb{R}^2$ is the metric

$$d(p, q) = \begin{cases} d(p, q) & p \text{ and } q \text{ lie on the same line through the origin} \\ d(p, 0) + d(0, q) & \text{otherwise} \end{cases}$$

This is indeed a metric. What are the open balls in this metric? They are the radial lines union an open ball around the origin, when $r$ is large enough.

These balls are not open in the usual topology, as the radial portion of these balls lack thickness in one direction. However, every ball in the usual topology on $\mathbb{R}^2$ is open in the French train metric. So $\mathcal{T}_T$ (the train metric) is finer than $\mathcal{T}$ (the usual topology).

14

<!-- page 15 -->

# 9/11/2019 - Subspaces, Products, Continuity

Recall that we were discussing bases for topological spaces. A basis is a smaller collection of open sets that generates a topology. Then in the topology generated by a basis $\mathcal{B}$, a set $U \subset X$ is open if for every point $x \in U$ there exists an element $B \in \mathcal{B}$ such that $x \in B \subset U$. In a metric space, the open balls are a basis for the metric space topology.

We also saw there is a more concrete description of the topology generated by a basis:

$$\mathcal{T} = \{\text{unions of elements of } \mathcal{B}\}$$

In other words, $\mathcal{T}$ is the coarsest topology which contains $\mathcal{B}$.

We will continue today with some examples.⁵ The first two will be very useful techniques by which we can build topologies on sets.

Let $X$ be a topological space and $A \subset X$ any subset. Recall that, if $X$ is a metric space, then $A$ inherits the metric space topology via the induced metric obtained from restricting the metric on $X$. Namely, the open balls in $A$ are of the form

$$B_r^A(p) = B_r^X(p) \cap A = \{x \in A : d(x, p) < r\}$$

Then we find that open subsets of $A$ are precisely the open sets of $X$ intersect $A$. This is because for an open $U \subset A$ we have

$$U = \bigcup_{p \in U} B_{r_p}^A(p) = \bigcup_{p \in U} B_{r_p}^X(p) \cap A = \left( \bigcup_{p \in U} B_r^X(p) \right) \cap A$$

where $r_p > 0$ is chosen such that $B_{r_p}^A(p) \subset U$. This motivates the following definition.

**Definition.** Let $X$ be a topological space and $A \subset X$ be a subset. The **subspace topology** on $A$ is

$$\mathcal{T}_A = \{U \cap A : u \in \mathcal{T}_X\}$$

**Lemma.** $\mathcal{T}_A$ is indeed a topology on $A$. Furthermore, if $\mathcal{B}$ is a basis for $\mathcal{T}_X$ then $\{B \cap A : B \in \mathcal{B}\}$ is a basis for $\mathcal{T}_A$.

Proof. Clearly $\varnothing, A \in \mathcal{T}_A$, as $\varnothing, X \in \mathcal{T}_X$. We also have

$$\bigcup_i (U_i \cap A) = \left( \bigcup_i U_i \right) \cap A$$

$$\bigcap_{i=1}^n (U_i \cap A) = \left( \bigcap_{i=1}^n U_i \right) \cap A$$

⁵Munkres, sections 14-16.

15

<!-- page 16 -->

so $\mathcal{T}_A$ is closed under arbitrary unions and finite intersections, as $\mathcal{T}$ is.

Also, using the above characterization of a basis, for an open set $U \subset X$ we can write

$$U \cap A = \left( \bigcup_i U_i \right) \cap A = \bigcup_i U_i \cap A$$

So any open set in $\mathcal{T}_A$ can be expressed as the union of elements of $\{B \cap A : B \in \mathcal{B}\}$, which completes the proof.

**Remark.** *The closed sets in the subset topology on $A \subset X$ are of the form $Y \cap A$, where $Y \subset X$ is closed.*

This is an easy set-theoretic verification.

### Examples

- The subspace topology on $\mathbb{R} \subset \mathbb{R}^2$ is the usual topology on the real line.
- Consider the subspace topology on $[0, 1] \subset \mathbb{R}$. The open intervals that are proper subsets of $[0, 1]$ are open as usual. But the half-interval $[0, 1/2)$ is also open in $[0, 1]$ as it can be obtained via the intersection $[0, 1] \cap (-1/2, 1/2)$.
- With the subspace topology on $\mathbb{Q} \subset \mathbb{R}$ some sets now can be both open and closed. For example, $(\sqrt{2}, \sqrt{3}) \cap \mathbb{Q}$ is open, but it is also closed, as $(\sqrt{2}, \sqrt{3}) \cap \mathbb{Q} = [\sqrt{2}, \sqrt{3}] \cap \mathbb{Q}$.

### The product topology

We will begin by discussing topologies on finite products. For infinite products, however, the obvious generalization breaks down. We will see this a bit later.

**Definition.** *Given topologies $\mathcal{T}$ on $X$ and $\mathcal{T}'$ on $Y$, the **product topology** on $X \times Y$ is the topology generated by the basis $\mathcal{B} = \{U \times V : U \in \mathcal{T}, V \in \mathcal{T}'\}$.*

Note that the set $\mathcal{B}$ is itself not a topology, as the union of two rectangles $U_1 \times V_1$ and $U_2 \times V_2$ is not necessarily another rectangle.

![img-4.jpeg](img-4.jpeg)

**Lemma.** *This set $\mathcal{B} = \{U \times V : U \in \mathcal{T}, V \in \mathcal{T}'\}$ is indeed a basis.*

16

<!-- page 17 -->

Proof. The sets of the form $U \times V$ cover, as the whole space $X \times Y$ is the product of $X \in \mathcal{T}$ and $Y \in \mathcal{T}'$. If $U_1 \times V_1, U_2 \times V_2 \in \mathcal{B}$, then

$$(U_1 \times V_1) \cap (U_2 \times V_2) = (U_1 \cap U_2) \times (V_1 \cap V_2)$$

Thus their intersection it itself an open rectangle, as $U_1 \cap U_2 \in \mathcal{T}$ and $V_1 \cap V_2 \in \mathcal{T}'$. Therefore $\mathcal{B}$ is indeed a basis.

Intuitively, the idea is that a point is close to $(x, y)$ if it is both close to $x$ and close to $y$.

There is in fact a better basis that generates the product topology.

Proposition. If $\mathcal{B}, \mathcal{B}'$ are bases for $\mathcal{T}, \mathcal{T}'$, respectively, then the product topology is generated by the basis

$$\mathcal{D} = \{B \times B' : B \in \mathcal{B}, B' \in \mathcal{B}'\}$$

Proof. This is because everything in $\mathcal{D}$ is indeed open, as these are products of open sets. Furthermore, every open set of $Z \subset X \times Y$ can be written

$$Z = \bigcup_i U_i \times V_i = \bigcup_i \left(\bigcup_j B_j\right) \times \left(\bigcup_k B'_k\right) = \bigcup_i \bigcup_j \bigcup_k B_j \times B'_k$$

### Example

- We have that the product topology on $\mathbb{R} \times \mathbb{R}$ is the usual topology on $\mathbb{R}^2$.

By the previous proposition a basis for $\mathbb{R} \times \mathbb{R}$ is given by

$$\{(a_1, b_1) \times (a_2, b_2) : a_1 < b_1, a_2 < b_2\}$$

These are also open in the standard topology on $\mathbb{R}^2$, because for any point $(x, y) \in (a_1, b_1) \times (a_2, b_2)$, the ball of radius $\min\{|x - a_1|, |x - a_2|, |x - b_1|, |x - b_2|\}$ is contained in $(a_1, b_1) \times (a_2, b_2)$.

Conversely, given an open ball $B$ in $\mathbb{R}^2$ and $x \in B$ we can choose a small enough open rectangle $R = (a_1, b_1) \times (a_2, b_2)$ with $x \in R \subset B$.

One can also show this easily using the metric

$$d_\infty((x, y), (x', y')) = \max\{|x - x'|, |y - y'|\}$$

The ball of radius $r$ centered at $p$ in this metric is the cube of side length $2r$ centered at $p$, namely the product $(x - r, x + r) \times (y - r, y + r)$, which is already a basis element of the product topology. Thus the topology induced by $d_\infty$, which is the standard topology on $\mathbb{R}^2$, is the product topology.

17

<!-- page 18 -->

**Definition.** Let $X$ be a set with a total order.$^{6}$ The **order topology** on $X$ is generated by the basis that contains the elements

- $(a, b) = \{x \in X : a < x < b\}$
- If $X$ has a smallest element $a_0$, then also the element $[a_0, b) = \{x \in X : a \leq x < b\}$
- If $X$ has a largest element $b_0$, then also the element $(a, b_0] = \{x \in X : a < x \leq b\}$

### Examples

- On $\mathbb{R}$ with the usual order, the order topology is the usual topology on $\mathbb{R}$.
- On subsets of $\mathbb{R}$ with the usual order, the order topology is the subspace topology.
- We can consider stranger examples as well. During this example, we will denote the point $(a, b) \in [0, 1] \times [0, 1]$ by $a \times b$ to eliminate confusion. Consider the lexigraphic/dictionary order defined on $[0, 1] \times [0, 1]$. This is defined by

$$a \times b < a' \times b' \iff a < a' \text{ or } (a = a' \text{ and } b < b')$$

Then the open sets are of the form

![img-5.jpeg](img-5.jpeg)

The open sets in the order topology are not open in the standard topology (obtained via the subspace topology inherited from $\mathbb{R}^2$), since there are no open neighborhoods of the edge points contained in $(a, b) \subset [0, 1] \times [0, 1]$.

Open sets in the standard topology are not necessarily open in the order topology either. An open ball in the interior of $[0, 1] \times [0, 1]$ is open in the order topology, as it is the union of vertical line segments. But if we examine the point $1/2 \times 0$ in the open set $[0, 1] \times [0, 1/2)$, it does not sit in any basis element of the order topology (open interval) that is contained in $[0, 1] \times [0, 1/2)$. This is because any open interval containing $1/2 \times 0$ must have starting point $a$ with $a < 1/2$. Then the interval contains all points on the vertical line with first coordinate $x$ for any $a < x < 1/2$, and these points are not all contained in $[0, 1] \times [0, 1/2)$.

$^{6}$A total order is a relation $<$ on $X \times X$ such that

1. Either $a < b$, $b < a$, or $a = b$ (precisely one of these must hold).

2. If $a < b$ and $b < c$, then $a < c$, namely $<$ is transitive.

18

<!-- page 19 -->

The above example illustrates a situation in which two topologies, namely the usual topology and dictionary order topology on $[0, 1] \times [0, 1]$ are not comparable.

## Continuity

**Definition.** Let $X, Y$ be topological spaces. A function $f : X \to Y$ is **continuous** if for all open $U \subset Y$, the preimage $f^{-1}(U) \subset X$ is open.

**Remark.** For metric spaces, this definition agrees with the delta-epsilon formulation of continuity.

Note that the continuity of a function depends entirely on the topology of the spaces involved.

### Examples

- Define the function $f : \mathbb{R} \to \mathbb{R}$ by

$$f(x) = \begin{cases} 1 & x \geq 0 \\ -1 & x < 0 \end{cases}$$

Consider an open set around $f(0) = 1$. The inverse image of the open set $(1/2, 1/3) \subset \mathbb{R}$ is $[0, \infty) \subset \mathbb{R}$, which is not open in the usual topology. Thus $f$ is not continuous.

- Equip $\mathbb{R}$ with the lower limit topology and denote this space by $\mathbb{R}_\ell$. Recall that the lower limit topology is finer than the usual topology. Then the function $f : \mathbb{R}_\ell \to \mathbb{R}_\ell$ defined as above is in fact continuous. This is because the set $f^{-1}((1/2, 3/2) = [0, \infty) \subset \mathbb{R}_\ell)$ is now open. In fact, for *every* open $U \subset \mathbb{R}_\ell$ the set $f^{-1}(U)$ is open. There aren't many choices, so we can explicitly compute

$$f^{-1}(U) = \begin{cases} \varnothing & \{-1, 1\} \cap U = \varnothing \\ [0, \infty) & 1 \in U \text{ and } -1 \notin u \\ (-\infty, 0) & -1 \in U \text{ and } 1 \notin U \\ \mathbb{R} & -1, 1 \in U \end{cases}$$

All of these are open in the lower limit topology, which proves that $f : \mathbb{R}_\ell \to \mathbb{R}_\ell$ is continuous.$^a$

- The identity function $f : \mathbb{R} \to \mathbb{R}_\ell$, defined by $f(x) = x$, is *not* continuous. This is because the preimage of $[0, 1) \subset \mathbb{R}_\ell$ is $[0, 1) \subset \mathbb{R}$, which is not open. The identity function $f : \mathbb{R}_\ell \to \mathbb{R}$ is continuous, as any open set $U \subset \mathbb{R}$ is open in $\mathbb{R}_\ell$. This demonstrates that we can gauge the fineness of a topology relative to another topology on the same set by the continuity of the identity map.
- Let $X, Y$ be topological spaces. The projection $\pi_1 : X \times Y \to X$ defined by $\pi(x, y) = x$ is continuous. This is because any open set $U \subset X$ has preimage $\pi_1^{-1}(U) = U \times Y$, which is open on the product space.

$^a$In fact, the topology on the codomain here is irrelevant. As long as the domain is $\mathbb{R}_\ell$, this $f$ will be continuous.

19

<!-- page 20 -->

Next class we will speak further about continuity and show that it suffices to check continuity on a basis. We will also define the notion of a *homeomorphism*, which captures when two spaces are topologically the same.

20

<!-- page 21 -->

# 9/16/2019 - Continuity, Homeomorphisms, Limit Points

Today we will continue discussing continuity and then begin speaking about limit points.

# Continuity

Recall the following definition.

Definition. A function $f : X \to Y$ is continuous if for all open $U \subset Y$, $f^{-1}(U) \subset X$ is open.

It in fact suffices to check continuity on a basis. This provides a criterion that is often more convenient that looking at all open sets.

Proposition. A function $f : X \to Y$ is continuous if and only if for all basis elements $B \subset Y$ for the topology on $Y$, $f^{-1}(B) \subset X$ is open.

Proof. This condition is certainly necessary, as every basis element for the topology on $Y$ is open in $Y$. It is also sufficient, as an open set $U \subset Y$ can be written $U = \bigcup_i B_i$, in which case we have that

$$f^{-1}(U) = f^{-1}\left(\bigcup_i B_i\right) = \bigcup_i f^{-1}(B_i) \subset X$$

is open.

# Example

- If $X$ is a topological space and $Y$ is a metric space, then it suffices to check that $f^{-1}(B_\epsilon(y)) \subset X$ is open for all $y \in Y$ and $\epsilon > 0$. If we expand this to the case when $X$ is also a metric space, we will find that this definition is a bit stronger than the usual definition of continuity for metric spaces (as we demand that every point in $B_\epsilon(y)$ has a neighborhood around its preimage contained in the preimage of $B_\epsilon(y)$, rather than just considering the center $y$. Ultimately, however, these definitions are equivalent).

Since topological spaces can be quite pathological, it is worthwhile to confirm some basic, desirable properties of continuity.

Proposition. We have the following:

1. A constant function \( f: X \to Y \) given by \( f(x) = y_0 \) for all \( x \in X \) and some \( y_0 \in Y \) is continuous.
2. Let \( A \subset X \) be a subspace with the subspace topology. Then the inclusion \( i: A \hookrightarrow X \) is continuous.[7]
3. If \( f: X \to Y \) and \( g: Y \to Z \) are continuous, then the composition \( g \circ f: X \to Z \) is continuous.

7We can describe the subspace topology as the coarsest topology for $A$ such that this inclusion map is continuous.

21

<!-- page 22 -->

Note that we are not considering the sum or products of continuous functions for two reasons. The first is that these topological spaces may not have any addition or multiplication operations. The second is that, even if we are working with a space like $\mathbb{R}$, there are topologies for which the algebraic operations are not continuous.$^8$

Proof. Constant functions are continuous, since open sets $U \subset Y$ either contain $y_0$ or do not. If $y_0 \in U$, then the preimage of $U$ is all of $X$, which is open. Otherwise, the preimage of $U$ is empty, which is also open. Note that these are the only functions between two spaces that are always guaranteed to be continuous regardless of the topologies on $X$ and $Y$.

Let $U \subset$.

Let $U \subset Z$ be open. Then $g^{-1}(U)$ is open by continuity of $g$. And $f^{-1}(g^{-1}(U))$ is open by continuity of $f$. Thus $(g \circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$ is open. $\square$

It will be useful in algebraic topology to be able to say something about the continuity of a function given information about its behavior on certain pieces of a space.

Proposition. Let $X = \bigcup_i U_i$ with $U_i \subset X$ open, and let $f : X \to Y$ be a function such that the restriction $f|_{U_i} : U_i \to Y$ is continuous$^9$ for all $i$, then $f$ is continuous.

One can also recast this proposition to say that a function $f : X \to Y$ is continuous if, for every point in $X$, there is an open set of $X$ on which $f$ is continuous.

Also note that the converse of this proposition holds, since if $f$ is continuous then the restriction $f|_{U_i} : U_i \to Y$ is given as the composition of the inclusion $i : U_i \to X$ and $f$, which are both continuous.

Proof. For all $V \subset Y$ open, $(f|_{U_i})^{-1}(V) = f^{-1}(V) \cap U_i$, which is open in $U_i$ by assumption. Hence

$$(f|_{U_i})^{-1}(V) = U_i \cap (\text{open set in } X)$$

is open in $X$. In general, an open subset of an open subspace of $X$ is also open in $X$. Thus

$$f^{-1}(V) = f^{-1}(V) \cap \left( \bigcup_i U_i \right) = \bigcup_i f^{-1}(V) \cap U_i = \bigcup_i f|_{U_i}^{-1}(V)$$

and the sets $f|_{U_i}^{-1}(V)$ are open. $\square$

## Homeomorphism

What makes two topological spaces the same? We usually don't want to demand that two topological spaces are the same only if their underlying sets and topologies are precisely equal. Every branch of math has a notion of sameness$^{10}$, and in topology this notion is homeomorphism.

$^8$Topological spaces with a continuous operation defined on them are called topological groups.

$^9$Where $U_i$ is of course given the subspace topology.

$^{10}$For example, two vector spaces are the same if they are isomorphic.

22

<!-- page 23 -->

**Definition.** A **homeomorphism** is a bijection $f: X \to Y$ such that $f: X \to Y$ and $f^{-1}: Y \to X$ are both continuous.

Intuitively, the continuity of both $f$ and $f^{-1}$ means we have bijections

![img-6.jpeg](img-6.jpeg)

So a set $U \subset X$ is open if and only if $f(U) \subset Y$ is open. In other words, points in $X$ are close together if and only if their images are close together in $Y$.

**Definition.** Spaces $X$ and $Y$ are **homeomorphic** if there exists a homeomorphism $f: X \to Y$.

**Remark.** A continuous bijection need not be a homeomorphism.

### Nonexamples

- The identity id: $\mathbb{R}_{\ell} \to \mathbb{R}$ is a continuous bijection, but it is not a homeomorphism. It is continuous because $\mathbb{R}_{\ell}$ is finer than the standard topology $\mathbb{R}$. But $[a, b) \subset \mathbb{R}_{\ell}$ is open in $\mathbb{R}_{\ell}$ but not in $\mathbb{R}$.
- Let $X = \{0\} \cup \{1/n : n \in \mathbb{N}\}$ as a subspace of $\mathbb{R}$ and consider $\mathbb{N}$ with the discrete topology (which is also the subspace topology inherited from $\mathbb{R}$). Consider the bijection $f: \mathbb{N} \to X$ defined by $f(0) = 0$ and $f(n) = 1/n$. $f$ is continuous, as any function from a space with the discrete topology is continuous.$^a$ The inverse bijection is not continuous. $\{0\}$ is open, but the image $f(\{0\}) = \{0\} \subset X$ is not open. This is because any open ball around $0$ in $\mathbb{R}$ contains some $1/n$.

$^a$This is because any subset of $\mathbb{N}$ is open, so the preimage of every subset of the codomain is open.

Recall the following definition.

**Definition.** A metric space $X$ is **bounded** if $\sup\{d(x, y) : x, y \in X\}$ is finite.

In turns out that this is *not* a topological property.

### Boundedness is not topological

- Consider the function $f: (-\pi/2, \pi/2) \to \mathbb{R}$ defined by $f(x) = \tan x$. $f$ is a continuous bijection from $(-\pi/2, \pi/2)$ to $\mathbb{R}$ with a continuous inverse arctan. Thus $f$ is a homeomorphism from $(-\pi/2, \pi/2)$ to $\mathbb{R}$.

So two topological spaces can be homeomorphic despite the fact that one is bounded and the other is not. Intuitively, topologies do not detect *how* far points are from each other, but rather only if points are *close* to each other.

Homeomorphism is what makes the sameness of topological spaces precise. There is a related notion that describes when one space looks like a subspace of another.

23

<!-- page 24 -->

**Definition.** *An **embedding** is a continuous injective map $f: Y \to X$ such that the induced map $f: Y \to f(Y) \subset X$ is a homeomorphism, where $f(Y) \subset Y$ is equipped with the subspace topology.*

Note that in this class, we are not considering the smoothness of an embedding.$^{11}$

### Closed sets and limit points$^{12}$

Recall that a subset $A \subset X$ is closed if its complement $X \setminus A$ is open. Subsets can be both open and closed. They can also be neither open nor closed. We can approximate subsets with open and closed sets.

**Definition.** *Let $A \subset X$ be any subset. The **closure** of $A$, denoted by $\overline{A}$, is the smallest closed set containing $A$. It is given by*

$$\overline{A} = \bigcap_{Y \supset A \text{ closed}} Y$$

Note that if $A$ is already closed, then $\overline{A} = A$. If $\overline{A} = A$ then $A$ is closed. We will see that $\overline{A}$ is obtained from $A$ by adding points.

**Definition.** *A subset $A \subset X$ is **dense** if $\overline{A} = X$.*

**Definition.** *Let $A \subset X$ be any subset. The **interior** of $A$, denoted by $\operatorname{int}(A)$, is the largest open closed containing $A$. It is given by*

$$\operatorname{int}(A) = \bigcup_{U \subset A \text{ open}} U$$

The interior of $A$ consists of all the interior points of $A$, which are points in $A$ that have an open neighborhood contained in $A$.

Note that if $A$ is already open, then $\operatorname{int}(A) = A$. If $\operatorname{int}(A) = A$ then $A$ is open.

**Definition.** *Let $A \subset X$ be any subset. The **boundary** of $A$, denoted by $\partial A = \operatorname{bd}(A)$, is $\overline{A} \setminus \operatorname{int}(A)$.*

#### Example

- Let $X = [0, 1)$. Then $\overline{X} = [0, 1]$. $[0, 1]$ is closed and contains $[0, 1)$, and certainly $[0, 1) \subset \overline{X}$, so we only have to prove that $1 \in \overline{X}$. Suppose for contradiction $1 \notin \overline{X}$. Then $\overline{X} = [0, 1)$, which is not closed.

We have $\operatorname{int}(X) = (0, 1)$ for similar reasons, and then $\partial X = \{0, 1\}$.

It will be very useful to remember that if $A \subset F$ and $F$ is closed, then $\overline{A} \subset F$. Similarly, if $U \subset A$ and $U$ is open, then $U \subset \operatorname{int}(A)$. We also have

$$\overline{(X \setminus A)} = X - \operatorname{int}(A)$$

$^{11}$In differential geometry/topology, the cuspidal cubic cannot be obtained as an embedding of the line $\mathbb{R}$, as there is a lack of smoothness at the origin.

24

<!-- page 25 -->

### Example

- $\mathbb{Q} \subset \mathbb{R}$ is dense, namely $\overline{\mathbb{Q}} = \mathbb{R}$. Suppose the open set $\mathbb{R} \setminus \overline{\mathbb{Q}}$ is nonempty with $x \in \mathbb{R} \setminus \mathbb{Q}$. Then there is some $\epsilon > 0$ such that $(x - \epsilon, x + \epsilon) \subset \mathbb{R} \setminus \mathbb{Q}$. But every open interval of reals contains a rational number.

By the same argument and the density of the irrationals, $\operatorname{int}(\mathbb{Q}) = \varnothing$.

Thus $\partial(\mathbb{Q}) = \mathbb{R}$.

We will next introduce limit points, which are an important way of describing closedness.

**Definition.** A neighborhood of a point $x \in X$ is an open set $U \subset X$ with $x \in U$.

**Definition.** A point $x \in X$ is a **limit point** of a subset $A \subset X$ if for every neighborhood $U \subset X$ of $x$ there exists a point $a \in A$ with $a \neq x$ and $a \in U$.

Note that the condition that $a \neq x$ means that an isolated point of $A$ is not a limit point. Intuitively, limit points of $A$ are points for which there exist points of $A$ arbitrarily close to $x$.

It is an immediate consequence of the definition that all interior points and boundary points are limit points of $A$.

### Examples

- 1 is a limit point of the subset $(0, 1)$ or of $[0, 1]$. There are points arbitrarily close to 1 in these sets that are not equal to 1 itself.

- 1 is not a limit point of the set $\{0\} \cup \{1/n : n \in \mathbb{N}\}$, as small neighborhoods of 1 will contain only the element 1 from this set. However, 0 is indeed a limit point of this set.

This allows us to formulate the following characterization of the closure.

**Theorem.** We have

$$\overline{A} = A \cup \{\text{limit points of } A\}$$

Proof. Suppose $x \notin A$ and $x$ is not a limit point of $A$. Then there exists an open neighborhood $U \subset X$ of $x$ which doesn't contain anything from $A$. Thus $X \setminus U$ is a closed set that contains $A$ and $\overline{A} \subset X \setminus U \subset X \setminus \{x\}$. So $x \notin \overline{A}$.

Suppose $x \notin \overline{A}$. Then $x \in X \setminus \overline{A}$, which is an open set. Let $U \subset X \setminus \overline{A}$ be an open neighborhood of $x$. $U$ is disjoint from $A$, so $x$ is not in $A$ and is not a limit point of $A$ either. $\square$

**Definition.** $x \in \overline{A}$ if and only if, for every neighborhood $U \subset X$ of $x$ we have $A \cap U \neq \varnothing$.

This follows easily from the above theorem. Next time we will discuss the limit of a sequence and its relation to limit points.

25

<!-- page 26 -->

## 9/18/2019 - Sequences, Limits, Products

Today we will begin by discussing sequences and limits.¹³ Recall that we had the following definition:

**Definition.** *A point $x \in X$ is a **limit point** of $A \subset X$ if for all open neighborhoods $U$ of $x$, we have $U \cap (A \setminus \{x\}) \neq \varnothing$.*

We also proved the following theorem:

**Theorem.** *We have*

$$\overline{A} = \bigcap_{\substack{F \supset A \\ F \text{ closed}}} = A \cup \{\text{limit points of } A\}$$

**Corollary.** *$x \in \overline{A}$ if and only if for every neighborhood $U$ of $x$, we have $U \cap A \neq \varnothing$.*

**Definition.** *A sequence $x_1, x_2, \ldots$ in a topological space $X$ converges to a limit $x$ if for all neighborhoods $U$ of $x$, there exists $N \in \mathbb{N}$ such that $n \geq N$ implies $x_n \in U$.*

The limit of a sequence is not necessarily unique. We will see later what conditions need to be placed on $X$ in order to guarantee that limits are unique.

**Definition.** *A **basis of neighborhoods** for $x$ is a family of neighborhoods $\mathcal{B} = \{B_i\}$ of $x$ such that if $U$ is a neighborhood of $X$, there exists some $i$ with $B_i \subset U$.*

We can sharpen the criterion for converging to a limit.

**Remark.** *A sequence converges to a limit $x$ if there exists such an $N \in \mathbb{N}$ for every element in a basis of neighborhoods for $x$.*

### Example

- In a metric space, the family $\{B_\epsilon(x) : \epsilon > 0\}$ forms a basis of neighborhoods for $x$.

The family $\{B_{1/n}(x) : n \in \mathbb{N}\}$ also forms a basis of neighborhoods for $x$.

We can now see how the usual notion of convergence in a metric space is a special case of convergence in general topological spaces.

### Convergence in metric spaces

- In a metric space, a sequence $x_1, x_2, \ldots$ converges to a limit $x$ if and only if for all $r > 0$, there exists $N$ such that $n \geq N$ implies $x_n \in B_r(x)$.

¹³Munkres, section 17

26

<!-- page 27 -->

Lemma. If there exists a sequence $x_1, x_2, \ldots$ in $A$ that converges to $x$ such that $x_n \neq x$ for all $n$, then $x$ is a limit point of $A$.

Conversely, in a metric space, if $x$ is a limit point of $A$, then for all $n \geq 1$, then there exists a sequence $x_1, x_2, \ldots$ that converges to $x$ with $x_n \neq x$.

To prove the converse in a metric space, we take $x_n \in B_{1/n}(x) \cap (A \setminus \{x\})$, which is nonempty by assumption.

In general, the disjointness assumption is to guarantee that $x_1, x_2, \ldots$ is not the constant sequence (without this assumption isolated points of $A$ would be declared limit points).

The converse also holds more generally in spaces whose points have countable bases of neighborhoods (these are called first-countable spaces$^{14}$). So to find a counterexample to the converse in general, it will be necessary to find a case in which there is a point with no countable basis of neighborhoods.

### A limit point without a converging sequence

- Consider the set $\mathbb{R}$ with the topology

$$\mathcal{T} = \{\varnothing\} \cup \{U : \mathbb{R} \setminus U \text{ is countable}\}$$

$\mathcal{T}$ is modeled after the finite-complement topology, and it is indeed a topology for similar reasons.

Let $A = (0, 1)$. We will show $A$ is dense. This is because if $F$ is a closed set that contains $A$, it must be countable. But there are no countable sets that contain $A$, so $F = \mathbb{R}$. Thus any real number is a limit point of $A$.

However, no sequence in $A$ converges to 2. Given any sequence $x_1, x_2, \ldots$ in $A$, the set $U = \mathbb{R} \setminus \{x_1, x_2, \ldots\}$ is an open set containing 2 that contains none of the points of the sequence. In fact, this same argument demonstrates that any sequence does not converge to any number. Thus the only sequences that converge are the sequences that eventually stabilize.

This is an example of a topology which has many limit points and for which it is very difficult for sequences to converge.

Intuitively, the notion of sequences indexed by the integers is suitable for capturing the idea of limit points in spaces that admit a countable description. To describe larger spaces like the above example using sequences would require a generalization of sequences indexed by (uncountable) sets.

$^{14}$A space is first-countable if for all $x$, there exit neighborhoods $U_1, U_2, \ldots$ such that for any neighborhood $V$ of $x$, there is some $n$ with $x \in U_n \subset V$. This is a way of making precise the complexity of a topology, and there is an entire classification system which extends this project.

27

<!-- page 28 -->

### Uniqueness of limits

In a metric space, the limit of a sequence, if it exists, is necessarily unique. This is not true in a general topological space.

#### Limits are not unique

- Consider the set \(\mathbb{R}\) with the finite complement topology

\[
\mathcal {T} = \{\varnothing \} \cup \{U: \mathbb {R} \setminus U \text {   is   finite } \}
\]

Let \( a_1, a_2, \ldots \) be a sequence in \( X \) with all \( a_i \) distinct. The claim is that this sequence converges to any element of \( \mathbb{R} \).

Let \( x \in R \), and consider a neighborhood U. Then U contains all but finitely many of the \( a_i \) points, so there exists N large enough so that \( n \geq N \) implies \( a_n \in U \).

\( ^{a} \) We actually only require that a point is hit by the sequence finitely many times.

At this point, the right thing to do is to introduce a notion that forces topological spaces to be better behaved.

#### Separation axioms

Definition. A topological space is Hausdorff, also called separable, if for distinct points  \( x_{1}, x_{2} \in X \)  there exist neighborhoods  \( U_{1} \)  of  \( x_{1} \)  and  \( U_{2} \)  of  \( x_{2} \)  such that  \( U_{1} \cap U_{2} = \varnothing \) .

![img-7.jpeg](img-7.jpeg)

#### Examples

- Metric spaces are Hausdorff. For points \( x, x_2 \in X \), let \( 0 < \epsilon < d(x_1, x_2)/2 \) and define \( U_1 = B_\epsilon(x_1) \) and \( U_2 = B_\epsilon(x_2) \). Then \( U_1 \cap U_2 = \varnothing \).
- The finite complement topology on \(\mathbb{R}\) is not Hausdorff. This is because any two nonempty open sets must intersect, as they both have finite complements.
- The discrete topology on any set is Hausdorff.

The following theorem motivates this definition.

28

<!-- page 29 -->

**Theorem.** *If X is Hausdorff, then every sequence converges to at most one limit.*

*Proof.* Assume there is a sequence $x_1, x_2, \ldots$ that converges to $x$ in $X$. Let $y \neq x$. We will show that this sequence does not converge to $y$. Since $X$ is Hausdorff, there exist open neighborhoods $U$ of $x$ and $V$ of $y$ such that $U \cap V = \varnothing$. By definition of convergence, there exists $N$ such that $n \geq N$ implies $x_n \in U$. Thus $V$ contains only finitely many points, so the sequence cannot converge to $y$. $\square$

The Hausdorff condition is one of many *separation axioms*, which are conditions that describe how well a topological space distinguishes between points. Most of the time in this course will be concerned with Hausdorff spaces, although non-Hausdorff topologies play an important role in many parts of math.$^{15}$ We have the following separation axioms:

1. A space $X$ is $T_0$ if, for distinct $x, y \in X$, there exists an open neighborhood of one that does not contain the other. This means that the open sets are enough to determine the points of $X$.
2. A space $X$ is $T_1$ if, for distinct $x, y \in X$, there exists an open neighborhood of $x$ not containing $y$ and an open neighborhood of $y$ not containing $x$. Equivalently, every singleton $\{x\}$ is closed.
3. A space $X$ is $T_2$ if it is Hausdorff, namely for distinct points $x, y \in X$, there exists an open neighborhood $U$ of $x$ and $V$ of $y$ such that $U \cap V = \varnothing$.
4. A space $X$ is $T_3$, also called *regular*, if it is $T_1$ and given a point $x \in X$ and closed $A \subset X$ that are disjoint, there exist neighborhoods $U$ of $x$ and $V$ of $A$ with $U \cap V = \varnothing$.$^a$
5. A space $X$ is $T_4$, also called *normal*, if for $A, B \subset X$ disjoint closed sets there exist open neighborhoods $U$ of $A$ and $V$ of $B$ with $U \cap V = \varnothing$.

$^a$Being Hausdorff is a weaker version of this condition when $A$ is taken to be the singleton. Munkres, section 31 contains examples of spaces that are $T_2$ but not $T_3$.

We see that $\mathbb{R}$ with the finite complement topology is $T_1$ (as singletons are closed) but not $T_2$. And $\mathbb{R}_\ell$ ($\mathbb{R}$ with the lower limit topology) is normal, while $\mathbb{R}_\ell \times \mathbb{R}_\ell$ is regular but not normal.

These axioms are important, for it is useful to know when a topological space arises from a metric space. A topological space that comes from a metric space is called **metrizable**. One way to approach this question is to determine where metric spaces lie in the hierarchy of separation axioms.

**Theorem.** *Every metric space is normal.*

The proof is not difficult but also not presently relevant to the course.

Conversely, we have the following theorem.

$^{15}$For example, in algebraic geometry the *Zariski topology* is a useful topology defined on space (or on the prime ideals of a commutative ring) that is not Hausdorff.

29

<!-- page 30 -->

**Theorem** (Urysohn Metrization theorem). *Every regular space with a countable$^{16}$ basis is metrizable.*

### Product topologies$^{17}$

We will see that when considering an infinite collection $\{X_i : i \in I\}$ of spaces, the question of the appropriate topology on their product

$$\prod_{i \in I} X_i = \{(x_i)_{i \in I} : x_i \in X, i \in I\} = \{\text{functions } f : I \to \bigcup X_i \text{ with } f(i) \in X_i \text{ for all } i \in I\}$$

becomes more complex. A first attempt might be the following:

**Theorem.** *The **box topology** on a product $\prod_{i \in I} X_i$ is generated by the basis*

$$\mathcal{B} = \left\{ \prod_{i \in I} U_i : U_i \subset X_i \text{ is open} \right\}$$

$\mathcal{B}$ is indeed a basis, as the intersection of two elements (open boxes) of $\mathcal{B}$ is another element of $\mathcal{B}$.

$$\left( \prod_{i \in I} U_i \right) \cap \left( \prod_{i \in I} V_i \right) = \prod_{i \in I} U_i \cap V_i$$

However, this will ultimately turn out to be an inappropriate topology for the general product space.

#### Example

- Consider the product

$$\mathbb{R}^N = \mathbb{R}^\omega = \mathbb{R}_0 \times \mathbb{R}_1 \times \mathbb{R}_2 \times \dots$$

Consider the diagonal map

$$\Delta : \mathbb{R} \to \mathbb{R}^\omega$$
$$x \mapsto (x, x, x, \dots)$$

In the finite case $\mathbb{R}^2$, the map $\Delta$ is the inclusion of $\mathbb{R}$ into the diagonal of the plane $\mathbb{R}^2$.

However, the diagonal map is *not* continuous in the box topology. For consider the open set

$$U = (-1, 1) \times (-1/2, 1/2) \times (-1/3, 1/3) \times \dots$$

$U$ is open in the box topology, as it is in fact a basis element. However, the preimage of $U$ under $d$ is precisely $\{0\}$, as we require

$$\Delta^{-1}(U) = (-1, 1) \cap (-1/2, 1/2) \cap (-1/3, 1/3) \cap \dots$$

$^{16}$There are stronger versions of the theorem that drop this countability condition, as sometimes it is useful to define metrics on large function spaces. However, this is at the cost of introducing much complexity.

30

<!-- page 31 -->

This is a good indication that the box topology is not the right one to take on the infinite product. We thus introduce the following topology.

**Definition.** *The **product topology** on a product $\prod_{i \in X} X_i$ is generated by the basis*

$$\mathcal{B} = \left\{ \prod_{i \in I} U_i : U_i \subset X_i \text{ is open and } U_i = X_i \text{ for all but finitely many } i \right\}$$

When $I$ is finite, the box topology and the product topology are equal. When $I$ is infinite, the product topology is strictly coarser than the box topology. With the product topology, we obtain the following important result:

**Theorem.** *A map $f : Z \to \prod_{i \in I} X_i$, where $\prod_{i \in I} X_i$ has the product topology, is continuous if and only if the component $f_i : Z \to X_i$ is continuous for all $i$.*

This justifies the choice of the product topology as the desired choice for an infinite product. We will prove one direction today.

*Proof.* Assume $f : Z \to \prod_{i \in I} X_i$ is continuous. The component maps are $f_i = p_i \circ f$, where $p_i$ is the projection to the $i$th factor. Each $p_i$ is continuous, as the preimage of $U \subset X_i$ is

$$p_i^{-1}(U) = \{(x_j)_{j \in I} : x_i \in U\} = \prod_{j \in I} U_j \text{ where } U_j = \begin{cases} X_j & j \neq i \\ U & j = i \end{cases}$$

The composition of continuous functions is continuous, so $f_i$ is continuous. $\square$

This argument did not require the product topology and would have worked equally well with the box topology. We will require the finiteness condition for the converse, which we will prove next time.

31

<!-- page 32 -->

# 9/23/2019 - More Product Topologies, Connectedness

We've been discussing lots of terminology and notation so far, and this will continue for a few more lectures. However, over the coming weeks, with connectedness and compactness, the material will involve more content.

Recall that we introduced two possible topologies on infinite product spaces.

$$X = \prod_{i \in I} X_i = \{(x_i)_{i \in I} : x_i \in X_i\} = \{\text{functions } f : I \to \bigcup_{i \in I} X_i \text{ with } f(i) \in X_i\}$$

$I$ can be any set (whether or not it is uncountable is irrelevant, and the theory becomes interesting only when $I$ is infinite of any cardinality). We defined the *box topology* as the topology generated by the basis

$$\mathcal{B}_{\text{Box}} = \left\{ \prod_{i \in I} U_i : U_i \subset X_i \text{ open} \right\}$$

The problem is that the box topology is too fine. So we instead introduced the *product topology*, which is generated by the basis

$$\mathcal{B}_{\text{Prod}} = \left\{ \prod_{i \in I} U_i : U_i = X_i \text{ for all but finitely many } i \right\}$$

The following characterization of continuity for maps into product spaces confirmed that the product topology is the right one to take on the product.

**Theorem.** *A function $f : Z \to X = \prod_{i \in I} X_i$ is continuous if and only if its components $f_i = \pi_i \circ f : Z \to Z_i$, where $\pi_i : X \to X_i$ is the usual projection, are continuous.*

For example, we considered the diagonal map

$$\Delta : \mathbb{R} \to \mathbb{R}^{\omega} = \mathbb{R}^{\mathbb{N}}$$

$$x \mapsto (x, x, \dots)$$

and saw that it is not continuous over the box topology, while by the theorem $\Delta$ is continuous when considered as a map into the product topology. Last time we proved one direction of the theorem, but we will review the result here.

*Proof.* Each projection $\pi : X \to X_i$ is continuous regardless of the topology on $X$, as for an open set $U \subset X_i$ we have

$$\pi_i^{-1}(U) = \{(x_j)_{j \in I} : x_i \in U\} = \prod_{j \in I} U_j$$

where $U_j = U$ if $j = i$ and $U_j = X_j$ otherwise. This is indeed open, so $f_i = \pi_i \circ f$ is the composition of continuous functions and hence continuous.

Conversely, suppose all $f_i$ component maps are continuous. We want to show $f$ is continuous,

32

<!-- page 33 -->

and it suffices to show that the inverse image of any basis element is open. Let $\prod_{i\in I}U_i\subset X$ be a basis element. Recall $U_{i} = X_{i}$ for all but finitely many $i$. We have

$$f ^ { - 1 } \bigg ( \prod _ { i \in I } U _ { i } \bigg ) = \{ z \in Z : f _ { i } ( z ) \in U _ { i } \} = \bigcap _ { i \in I } f _ { i } ^ { - 1 } ( U _ { i } )$$

Each $f_{i}^{-1}(U_{i})$ is open in $Z$ by the continuity of $f_{i}$. Furthermore, $f_{i}^{-1}(U_{i}) = Z$ whenever $U_{i} = X_{i}$, which happens for all but finitely many $i$. We thus have

$$f ^ { - 1 } \bigg ( \prod _ { i \in I } U _ { i } \bigg ) = \bigcap _ { j = 1 } ^ { n } f _ { i _ { j } } ^ { - 1 } ( U _ { i _ { j } } )$$

which is the finite intersection of open sets. Therefore $f$ is continuous.

The box and product topologies are likely the only natural/reasonable topologies to place on an arbitrary product of topological spaces. If our spaces are metric spaces, however, we can use their metrics to define another natural topology.

### Motivating example

- We defined a metric on $\mathbb{R}^n$ by

$$d _ { \infty } ( x , y ) = \sup _ { i \in \{ 1 , \dots , n \} } | y _ { i } - x _ { i } |$$

Recall that $d_{\infty}$ defines the same topology on $\mathbb{R}^n$ as the product topology.

The above example does not work immediately for infinite products, as the supremum of the individual distances may not exist (if the distances become arbitrarily large, for example).

One solution would be to restrict to sequences in the product with bounded distances, but this is not ideal, as we would like to consider the entire product space. Recalling that the only thing that matters in a topology is the relative distance between points, another solution is to replace every metric with a bounded metric that induces the same topology.

Let $(x_{i},d_{i})$, for $i\in I$, be a collection of metric spaces. For each $i$, define a new metric

$$\overline { { { d _ { i } } } } ( x , y ) = \operatorname* { m i n } \{ d ( x , y ) , 1 \}$$

This is still a metric. The only property to check is the triangle inequality, but this is not too difficult.

Lemma. $\overline{d_i}$ induces the same topology on $X_i$ as $d_i$.

Proof. A basis for the topology induced by $\overline{d_i}$ consists of balls of radius less than 1 in the $d_i$ metric as well as all of $X_i$. The key observation is that it doesn't hurt us to throw away the larger balls in the $d_i$ metric.

If $U$ is open in the $d_i$ metric, for each $x \in U$ there exists a radius $r$ ball around $x$. If $r \geq 1$, then we can just take a ball in the $\overline{d_i}$ metric of radius less than 1. Therefore $U$ is open in the $\overline{d_i}$ metric as well. The other direction is similar.

33

<!-- page 34 -->

**Definition.** Let $(X_i, d_i)$ be a collection of metric spaces. The **uniform topology** on the product $\prod_{i \in I} X_i$ is the topology induced by the **uniform metric**, defined by

$$\overline{d_{\infty}}(x, y) = \sup_{i \in I} \overline{d_i}(x_i, y_i)$$

### Example

- The uniform topology on $\mathbb{R}^I = \{\text{functions } I \to \mathbb{R}\}$ is defined by

$$\overline{d_{\infty}}(f, g) = \min \left\{ \sup_{i \in I} |f(i) - g(i)|, 1 \right\}$$

Then a sequence of functions $f_n$ converge to $f$ if and only if $\overline{d_{\infty}}(f_n, f)$ converges to 0. This is the definition of *uniform convergence*.

To understand the topology that the uniform metric defines, we must first understand the open balls. If $I$ is finite, then the open balls of radius $r \le 1$ for $\overline{d_{\infty}}$ are products of balls of radius $r$.

$$B_r^{\overline{d_{\infty}}}(x) = \prod_{i \in I} B_r^{\overline{d_i}}(x_i)$$

This is simply because the supremum of the individual distances is less than $r$ if and only if all of the individual distances are less than $r$.

This situation becomes a bit more complex with an infinite product. For example, the set

$$U = (-1, 1) \times (-1, 1) \times \dots \subset \mathbb{R}^{\omega}$$

is *not* the unit ball around in the origin with the uniform metric. The unit ball is indeed in $U$, but the point $(0, 1/2, 2/3, 3/4, \dots)$ is contained in $U$ but not the unit ball, as

$$\overline{d_{\infty}}(0, 1/2, 2/3, 3/4, \dots) = \sup\{0, 1/2, 2/3, 3/4, \dots\} = 1$$

which is not strictly less than 1.

In fact, $U$ is not even open. For any $\epsilon$-ball around the above point contains points outside of $U$ (we can choose some coordinate sufficiently close to 1 such that adding $\epsilon$ moves outside of $U$). Despite this setback, we can indeed formulate a description of open balls. If $r \le 1$, then for $r' < r$ define

$$U_{r'}(x) = \prod_{i \in I} B_{r'}^{\overline{d_i}}(x)$$

$U_{r'}$ is contained in $B_r^{\overline{d_{\infty}}}(x)$. The idea is that we bound each element of the tuple by some safety margin from 1. In other words, if every coordinate is less than $1 - \epsilon$, then their supremum will be no more than $1 - \epsilon < 1$.

Conversely, if $\overline{d_{\infty}}(x, y) < r$, then there exists $r' < r$ such that $\overline{d_{\infty}}(x, y) < r' < r$. Therefore $\overline{d_i}(x, y) < r'$ for all $i$, and thus $y \in U_{r'}(x)$. This proves that $x \in B_r^{\overline{d_{\infty}}}$ if and only if $x \in U_{r'}(x)$ for some $r' < r$. Thus

$$B_r^{\overline{d_{\infty}}}(x) = \bigcup_{r' < r} U_{r'}(x)$$

34

<!-- page 35 -->

In other words, we need that all components of a point are less than $r - \epsilon$ for some $\epsilon > 0$, not merely that they are all less than just $r$. We can now state the following theorem.

**Theorem.** *The uniform topology on a product of metric spaces is finer than the product topology and coarser than the box topology.*

**Remark.** *For a finite product, $\mathcal{T}_{prod} \subset \mathcal{T}_{unif} \subset \mathcal{T}_{box}$. It's obvious that $\mathcal{T}_{prod} = \mathcal{T}_{box}$ in this case, which implies that the three topologies are in fact equal.*

*Proof.* First we show that the uniform topology is finer than the product topology. Let $\prod_{i \in I} U_i$ be a basis element of the product topology. Let $x = (x_i)_{i \in I} \in \prod_{i \in I} U_i$. Since $x_i \in U_i$, there exists $r_i \in (0, 1]$ such that $B_{r_i}^{\overline{d_i}}(x_i) \subset U_i$.

The $r_i$ may all be different, so we take the smallest of all radii. Only finitely many $r_i$ are strictly less than 1 (explicitly, when $U_i = X_i$ take $r_i = 1$). If we take

$$r = \inf\{r_i : i \in I\}$$

then $r > 0$ and

$$B_r^{\overline{d_\infty}} \subset U_r(x) = \prod_{i \in I} B_r^{d_i}(x_i) \subset \prod_{i \in I} B_{r_i}^{\overline{d_i}}(x_i) \subset \prod_{i \in I} U_i$$

Therefore every open set in the product topology is open in the uniform topology.

Next we show that every ball in the metric $\overline{d_\infty}$ is open in the box topology. Balls with radius $r \ge 1$ are all of $X$ and hence open in the box topology. If $r < 1$ then

$$B_r^{\overline{d_\infty}}(x) = \bigcup_{r' < r} U_{r'}(x)$$

where

$$U_{r'}(x) = \prod_{i \in I} B_{r_i}^{\overline{d_i}}(x_i)$$

This expresses $B_r^{\overline{d_\infty}}$ as the union of open sets in the box topology, so it is also open in the box topology.

We could also ask whether or not the box and product topologies come from a metric when they are endowed on a product of metric spaces. In general, the box topology does not arise from a metric, while one can define a metric that induces the product topology on a set. We will not delve much further into this matter.

### Connectness

We will introduce the notion of connectedness today and continue with it next lecture.18 Intuitively, the idea of connectedness should be quite clear: a space is connected if it does not consist of two disjoint components. The trick will be to make this precise.

18Munkres, sections 23 and 24.

35

<!-- page 36 -->

**Definition.** A space $X$ is **connected** if it cannot be written $X = U \cup V$, where $U, V$ are disjoint, nonempty, open subsets. Such a decomposition is a **separation** of $X$.

Note that if $X = U \cup V$ is a separation, then $U = X \setminus V$ and $V = X \setminus U$ are both closed as well. We can then equivalently characterize connectedness as follows.

**Definition.** A space $X$ is **connected** if $A \subset X$ is open and closed implies $A = \varnothing$ or $A = X$.

When writing proofs, it is a useful strategy that if one can express a connected space $X = U \cup V$ with $U, V$ disjoint and open, then one of these sets is empty and the other is the whole space.

### Examples

- The subspace $[0, 1] \subset \mathbb{R}$ is connected. It's not completely obvious why, however, as on the other hand the subset $[0, 1] \cap \mathbb{Q}$ is not connected (one can cut the interval in half at any irrational number).

Suppose for contradiction we have a separation $[0, 1] = U \cup V$. We can assume $0 \in U$. Since $U$ is open, in fact $[0, \epsilon) \subset U$ for some $\epsilon > 0$. Define

$$a = \sup\{x > 0 : [0, x) \subset U\}$$

We have seen $a > 0$, as $a \geq \epsilon$. The first claim is that $a \notin V$. Indeed, if $a \in V$ and $V$ is open, there exists $\epsilon > 0$ such that $(a - \epsilon, a] \subset V$. But then $[0, x) \not\subset U$ whenever $x > a - \epsilon$, which contradicts the fact that $a$ is the supremum of all such $x$.

Thus $a \in U$. The second claim is that $a \not< 1$. Indeed, if $a < 1$ since $U$ is open there exists $\epsilon > 0$ such that $(a - \epsilon, a + \epsilon) \subset U$. Thus $[0, a + \epsilon) \subset U$, which contradicts the fact that $a$ is the supremum of all such $x$. Thus $a = 1$, which implies $[0, 1) \subset U$ and $1 \in U$. Therefore $V = \varnothing$, so $[0, 1]$ is connected.

- The subspace $[0, 1) \cup (1, 2] \subset \mathbb{R}$ is not connected. In general, if $A \subset \mathbb{R}$ where $x < y < z$ with $x, z \in A$ and $y \notin A$, then $A$ is not connected. So connected subsets of $\mathbb{R}$ must be 'interval-like.'

The above proof that $[0, 1]$ is connected seems more complex than it should be, but the underlying idea behind it is quite simple. We show that given a single point in $U$, it must follow that all points are in $U$ from the properties of the set in question (here, we use that nonempty bounded subsets of $\mathbb{R}$ have a least upper bound).

36

<!-- page 37 -->

## 9/25/2019 - Connectedness, Path Connectedness

We will return to the topic of connectness, which intuitively captures the idea when a space consists of a single piece. Recall the following definition.

**Definition.** *A topological space $X$ is **connected** if it doesn't have a separation $X = U \cup V$, where $U, V$ are nonempty, disjoint, open subsets.*

Equivalently, $X$ is connected if its only subsets that are both open and closed are $\varnothing$ and $X$. To prove that a space is not connected, it suffices to find a separation. It can be trickier to prove that a space is connected, but the typical strategy is to show why one of the subsets must in fact be the entire space. We will see examples of this today.$^{19}$

We also saw last time that connected subsets of $\mathbb{R}$ cannot have gaps (missing points).

### Examples

- $\mathbb{R}_{\ell}$, which is $\mathbb{R}$ with the lower limit topology,$^a$ is not connected. For example, $(-\infty, 0)$ and $[0, \infty)$ are both open, disjoint, and cover $\mathbb{R}_{\ell}$.

In fact, any subset of $\mathbb{R}_{\ell}$ with more than one point is disconnected by this same argument. Such a topological space is called *totally disconnected*.

- $\mathbb{R}$ with the finite complement topology is connected. If we write $\mathbb{R} = U \cup V$ with both $U$ and $V$ open, necessarily $U \cap V \neq \varnothing$ (as each of them does not contain only finitely many points).

Note that this example has a different flavor. Usually it is difficult to find open sets that exactly tile a space, but here it is impossible to find nonempty open sets that are even disjoint.

$^a$Intuitively, one should imagine $\mathbb{R}_{\ell}$ as the real line with a gap to the left of each point (as there are open neighborhoods which do not contain any points less than a particular point) but with points to the right of that point.

The idea of connectedness will be important later, when we study algebraic topology. Generalizations of connectedness are an important tool that topologists use to distinguish between spaces.

Let $A, B \subset X$ be connected. It is not necessarily true that $A \cap B$ is connected. It is easy to find a counterexample in $\mathbb{R}^2$.

The union of connected spaces is also not necessarily connected. However, we can come up with a condition to guarantee that the union of such spaces is in fact connected.

**Proposition.** *Let $A, B \subset X$ be connected and suppose $A \cap B \neq \varnothing$. Then $A \cup B$ is connected.*

We can generalize this to infinite unions.

$^{19}$Recall the proof from last time that $[0, 1]$ is connected (which proceeded in this manner).

37

<!-- page 38 -->

**Theorem.** Let $A_i \subset X$ be a collection of connected subsets indexed by $I$ that all contain a point $p$. Then $Y = \bigcup_{i \in I} A_i$ is connected.

*Proof.* Let $Y = U \cup V$, with $U, V$ open sets. Either $U$ or $V$ contains $p$, so assume $p \in U$. Write $A_i = (U \cap A_i) \cup (V \cap A_i)$. Necessarily $U \cap A_i$ is not empty, so by connectedness of $A_i$ we have $A_i = U \cap A_i$ and $A_i \subset U$ (and $A_i \cap V = \varnothing$). This holds for all $i$ so $\bigcup_{i \in I} A_i \subset U$ and $Y = U$, $Y \cap V = \varnothing$. Therefore $Y$ is connected. $\square$

**Corollary.** $\mathbb{R}$ is connected. $[a, b], [a, b), (a, b) \subset \mathbb{R}$ are connected.

*Proof.* Write

$$R = \bigcup_{n \in \mathbb{N}} [-n, n]$$

Each $[-n, n]$ is connected by the argument from last time (as it is homeomorphic to $[0, 1]$). Thus $\mathbb{R}$ is connected. A similar argument shows these other intervals are also connected. $\square$

Note that we used the fact that if $X$ is homeomorphic to $Y$ and $X$ is connected, then $Y$ is also connected. For we can take the image of any separation of one of the sets under the homeomorphism to obtain a separation of the other set. In general, we can examine the behavior of connectedness under continuous functions.

**Theorem.** Let $f : X \to Y$ be a continuous function. If $X$ is connected, then $f(X) \subset Y$ is connected.

*Proof.* Note that what is outside the image of $f$ is irrelevant, so we can assume $f$ is surjective (as the corestriction $f : X \to f(X)$, where $f(X) \subset Y$ is given the subspace topology, is continuous).

If $f(X) = U \cup V$ with $U, V$ open, disjoint, and nonempty, then we can write $X = f^{-1}(U) \cup f^{-1}(V)$. These two sets are open, as $f$ is continuous. They are disjoint, as a single point cannot map to both $U$ and $V$ (which are disjoint). They are nonempty, as we assumed $f$ is surjective. Thus a separation of $f(X)$ implies there exists a separation of $X$. So if $X$ is connected, then $f(X)$ is connected as well. $\square$

The key idea of the proof is that the inverse image of a separation along a surjective continuous map is a separation of the domain. This observation implies the intermediate value theorem.

**Theorem.** Let $X$ be a connected topological space and $f : X \to \mathbb{R}$ a continuous function. Let $a, b \in X$ and $r \in \mathbb{R}$ be such that $f(a) < r < f(b)$. Then there exists $c \in X$ such that $f(c) = r$.

*Proof.* Suppose for contradiction $f(c) \neq r$ for all $c \in X$. Then $f(X) \cap (-\infty, r)$ and $f(X) \cap (r, \infty)$ is a separation of $f(X)$. But $X$ is connected, so $f(X)$ is connected, which is a contradiction. Therefore there exists some $c \in X$ with $f(c) = r$. $\square$

38

<!-- page 39 -->

It turns out that if we have any path in $X$ between two points, then along the path $f$ obtains all intermediate values.

We will continue by exploring how to build connected spaces from other connected spaces.

**Theorem.** *If $X$ and $Y$ is connected, then $X \times Y$ is connected.*

*Proof.* Let $X \times Y = U \cup V$, where $U, V$ are open and disjoint. Let $(a, b) \in U$. We will show that $U$ contains everything.

First, note that if we move along the slice $X \times \{b\} \subset X \times Y$, this space is connected. This is because the subspace topology on $X \times \{b\} \subset X \times Y$ is the same as the topology on $X$ (these spaces are homeomorphic). We have

$$X \times \{b\} = ((X \times \{b\}) \cap U) \cup ((X \times \{b\}) \cap V)$$

where these sets are open and disjoint. Since $(a, b) \in (X \times \{b\}) \cap U$, we have that $X \times \{b\} \subset U$. The same argument implies that $\{a\} \times Y$ is in $U$. In fact, since $\{x\} \times \{b\}$ is in $U$, any slice $\{x\} \times Y$ is in $U$ by the same argument. This holds for all $x \in X$, so $X \times Y \subset U$.$^{20}$

**Corollary.** *If $X_1, \ldots, X_n$ are connected, then their product $X_1 \times \ldots \times X_n$ is connected.*

It is true, but not obvious, that the infinite product of connected spaces is connected.

**Theorem.** *Let $(X_i)_{i \in I}$ be a collection of connected spaces, then their product $\prod_{i \in I} X_i$ (equipped with the product topology) is connected.*

We will see in a moment that this is not true in the box topology or the uniform topology. We won't use this result, so the proof is left as an exercise.

# Nonconnectedness of the infinite product

- Consider the product space

$$\mathbb{R}^{\omega} = \{(a_1, a_2, \ldots) : a_i \in \mathbb{R}\}$$

with the box topology. Let $U$ be the set of bounded sequences, such that for $(a_i)_i \in U$ there exists $M$ with $|a_i| < M$ for all $i$. Let $V$ be the set of unbounded sequences.

Clearly $U$ and $V$ are nonempty, disjoint, and cover $\mathbb{R}^{\omega}$. Then the only claim is that $U$ and $V$ are open in the box and uniform topologies. Since the box topology is finer than the uniform topology, it in fact suffices to check the uniform topology. But for the sake of completeness we will present both verifications.

$^{20}$Munkres supplies another proof. He argues to take the union of $(X \times \{b\} \cup \{x\} \times Y)$ for all $x$. All of these are connected, as they are individually the union of two slices (which are connected) that intersect at $(a, b)$. Furthermore, they all contain $(a, b)$, and hence their union is connected.

39

<!-- page 40 -->

Given a sequence \((a_{i})_{i}\in \mathbb{R}^{\omega}\), the basis element

\[
B _ {a} = \prod_ {i} (a _ {i} - 1, a _ {i} + 1)
\]

contains \((a_{i})_{i}\). If \((a_{i})_{i} \in U\) and \(M\) is a bound for \((a_{i})_{i}\), then \(M + 1\) is a bound for any sequence in \(B_{a}\). Thus \((a_{i})_{i} \in B_{a} \subset U\). If \((a_{i})_{i}\) is unbounded, then every sequence is \(B_{a}\) is also unbounded (as modifying the sequence coordinatewise by at most 1 does not affect boundedness). Therefore \(U\) and \(V\) are both open.

For the uniform topology, simply observe that the ball  \( B_{a} \)  contains the open ball in the uniform topology of radius 1 centered at  \( (a_{i})_{i} \)  (since the open balls of the uniform topology are a bit smaller than those of the box topology).

#### Path connectedness

Path connectedness is another way of precisely formulating the intuition that a space is made of one piece. We require the following definition.

Definition. If \( x, y \in X \), a path in \( X \) is a continuous map \( f: [0,1] \to X \) such that \( f(0) = x \) and \( f(1) = y \).

The only requirement on a path is that it be continuous (they do not need to be injective). Later in the course we will consider spaces of paths as an invariant for distinguishing topological spaces.

Definition. A space X is path-connected if any two points  \( x, y \in X \)  can be joined by a path.

Remark. The relation  \( \sim \)  defined by  \( x \sim y \)  if and only if there exists a path from x to y in X is an equivalence relation. \( ^{21} \)  The equivalence classes of this relation are called the path components of X.

It is now natural to ask about the relationship between connectedness and path-connectedness.

Theorem. If \( X \) is path connected, then \( X \) is connected.

Proof. Suppose \( X \) is path connected. Write \( X = U \cup V \), with \( U, V \) open and disjoint, with at least \( U \) nonempty. Let \( x \in U \). For any \( y \in X \), there exists a path \( f: [0,1] \to X \) from \( x \) to \( y \). Since \( [0,1] \) is connected, \( f([0,1]) \) is connected. Writing

\[
f ([ 0, 1 ]) = (f ([ 0, 1 ]) \cap U) \cup (f ([ 0, 1 ]) \cap V)
\]

implies \( f([0,1]) \subset U \), and in particular \( y \in U \) for all \( y \in X \).

\( ^{21} \) A relation that is reflexive, symmetric, and transitive. Such relations provide a notion of equality on a collection. The constant path demonstrates  \( \sim \)  is reflexive. To show  \( \sim \)  is symmetric, run a path from x to y backwards to obtain a path from y to x. Given paths from x to y and y to z, concatenate them to obtain a path from x to z.

40

<!-- page 41 -->

However, the converse is false. The famous counterexample is the *topologist's sine curve*, which is the subset of $\mathbb{R}^2$ defined by

$$S = \underbrace{\{(x, y) : y = \sin(1/x), x > 0\}}_{S_0} \cup \{(0, 0)\}$$

![img-8.jpeg](img-8.jpeg)

$S_0$ is connected, as it is the image of $(0, \infty)$ under a continuous function. We must confirm that adding $(0, 0)$ doesn't disconnect the space $S$.

Note that $(0, 0)$ is a limit point of $S$, as the sequence $\{(1/(n\pi), 0) : n \in \mathbb{N}\}$ converges to $(0, 0)$. Now write $S = U \cup V$, with $U, V$ open, nonempty, and disjoint. $S_0$ is either entirely in $U$ or $V$ by connectedness. Suppose $S_0 \subset U$. But since $U$ is closed, it contains its limit points. In particular, it contains $(0, 0)$, so $S = U$ and $V = \varnothing$.

However, $S$ is not path connected. The idea of the proof is as follows. Suppose for contradiction there exists a path $f : [0, 1] \to S$ with $f(0) = (0, 0)$ and $f(1, \sin 1)$. Composing with the projection to the $x$-axis yields a continuous function $\pi_x \circ f$. The intermediate value theorem implies that $\pi_x \circ f$ passes through all points of the form $p_n = 1/(2n\pi + \pi/2)$. There exist $t_n \in [0, 1]$ such that $f(t_n) = p_n$ for all $n$. Then the $p_n$ converge to 0, while for all $t_n$ we have that $f(t_n) = 1$.

However, the situation is not entirely hopeless. For well-behaved subsets of $\mathbb{R}^n$, these notions coincide.

**Theorem.** *If $A \subset \mathbb{R}^n$ is open, then $A$ is path-connected if and only if $A$ is connected.*

41

<!-- page 42 -->

## 9/30/2019 - Compactness

Today we will begin discussing what is perhaps one of the least intuitive notions in point set topology. Recall from real analysis that the closed interval $[a, b] \subset \mathbb{R}$ is *compact*. In fact, any closed and bounded set in $\mathbb{R}^n$ is compact. These sets enjoy nice properties, such as the fact that any continuous function $f : K \to \mathbb{R}$ from compact $K$ achieves its maximum and minimum. But in a general topological space, there is no notion of boundedness without a metric, so another definition will be necessary. Intuitively, compactness will be a generalization of a 'finiteness' for a space.

**Definition.** *Let $X$ be a topological space. A collection of open sets $\{U_i\}_{i \in I}$ is an **open cover** if $X = \bigcup_{i \in I} U_i$.*

Note that the index set $I$ can be anything, even uncountable.

**Definition.** *$X$ is **compact** if every open cover contains a finite subcollection that also covers $X$. Such a finite subcollection is a **finite subcover**.*

This can be a tricky definition. In order to show a space is compact, it is necessary to prove that *every* open cover has a finite subcover. Whereas to show a space is not compact, it is only necessary to exhibit a single open cover without a finite subcover.

### Examples

- $\mathbb{R}$ is not compact, as the cover

$$\mathbb{R} = \bigcup_{n \in \mathbb{Z}} (n, n + 2)$$

contains no finite subcover. Every open set is necessary, as removing any of them excludes the integer $n + 1$.

This is a good sign, as it indicates that the general definition of compactness we have given agrees with the usual one from analysis.

- The half-open interval $(0, 1]$ is not compact, The cover

$$(0, 1] = \bigcup_{n \in \mathbb{N}} (1/n, 1]$$

has no finite subcover.

- Let $X = \{0\} \cup \{1/n : n \in \mathbb{N}\}$. $X$ is compact. This is because some element of any open cover must contain 0, and thus contains all but finitely many of the points $\{1/n : n \in \mathbb{N}\}$. For each of the excluded points, take an open set that contains it. Then combining these we obtain a finite subcollection that covers $X$, so $X$ is compact.

**Theorem.** *If $A$ is compact and $f : A \to X$ is continuous, then $f(A)$ is compact.*

Note that if we take $X = \mathbb{R}$, then this recovers the result that continuous functions from compact spaces to $\mathbb{R}$ obtain their global extrema.

42

<!-- page 43 -->

*Proof.* Let $\{U_i\}_{i \in I}$ be an open cover of $f(A)$. The preimages $\{f^{-1}(U_i)\}_{i \in I}$ form an open cover of $A$. By compactness of $A$, there is a finite subcover $f^{-1}(U_1), \dots, f^{-1}(U_n)$ of $A$, where we are relabeling indices for the purposes of notation. Then $U_1, \dots, U_n$ cover $f(A)$, since their preimages cover $A$. Therefore $f(A)$ is compact. $\square$

The following is an important example that will allow us to greatly expand the theory of compact spaces.

*Proof.* Let $\{U_i\}_{i \in I}$ be an open cover of $[0, 1]$. Let

$$A = \{x \in [0, 1] : \text{there exists a finite subcover of } [0, x]\}$$

$A$ is nonempty, as it contains 0. We will show $A$ is both open and closed. Then by the connectedness of $[0, 1]$, this will prove $A = [0, 1]$.

- Suppose $x \in A$, namely $[0, x]$ admits a finite subcover. Then $x \in U_i$ for some $i$ in this finite subcover. $U_i$ is open, so there exists $\epsilon$ so that $B_\epsilon(x) \subset U_i$. Then $(x - \epsilon, x + \epsilon) \subset A$ as well, as the same finite subcollection is a finite subcover for any $[0, y]$ with $y \in (x - \epsilon, x + \epsilon)$. Therefore $A$ is open.
- To show $A$ is closed, let $x$ be a limit point of $A$. Then $x \in U_i$ for some $i$ in the cover, so $x \in B_\epsilon(x) \subset U_i$ for sufficiently small $\epsilon > 0$. There exists a point $y \in A$ with $|x - y| < \epsilon$, as $x$ is a limit point. Then the finite subcover of $[0, y]$ along with the set $U_i$ yields a finite subcover for $[0, x]$, so $x \in A$ and $A$ contains its limit points.

Therefore $A = [0, 1]$, which completes the proof. $\square$

In the usual topology on $\mathbb{R}^n$, compact sets are closed and bounded. Although there is no notion of boundedness in a general topological space, we can still ask how compactness is related to closedness.

**Theorem.** *If $X$ is compact, then any closed subspace $A \subset X$ is compact.*

*Proof.* Let $\mathcal{A}$ be an open cover of $A$ by sets open in $X$. Then $\mathcal{A} \cup \{X \setminus A\}$ is an open cover of $X$, which by compactness of $X$ admits a finite subcover. This yields a finite subcover of $A$. $\square$

So in a compact space, closed subsets are also compact. What about the converse? In $\mathbb{R}^n$, the answer is yes, but this fails more generally.

#### Compact does not imply closed

- Let $X \subset \mathbb{R}$, where $\mathbb{R}$ is given the cofinite topology. $X$ is always compact, as any open set contains all but finitely many points. So once we have one open set in a cover, it suffices to find finitely many remaining sets that cover the points missing from the first set.

43

<!-- page 44 -->

However, $X$ may not be closed. For example, any infinite set is not closed in the cofinite topology, although they are all compact.

However, we can salvage this by imposing conditions that ensure our topological spaces are not too pathological.

**Theorem.** *Let $X$ be Hausdorff. If $K \subset X$ is compact, then $K$ is closed.*

*Proof.* We will show that $X \setminus K$ is open. Let $x \in X \setminus K$. For every $y \in K$ there exists disjoint neighborhoods $y \in U_y$ and $x \in V_y$ by Hausdorffness. Then the collection $\{U_y\}_{y \in K}$ is a cover of $K$. By compactness, there exists a finite subcover $U_{y_1}, \dots, U_{y_n}$. The finite intersection $V = V_{y_1} \cap \dots \cap V_{y_n}$ is open and does not meet any $U_{y_i}$, and hence $V \cap K = \varnothing$. $V$ is an open neighborhood of $x \in X \setminus K$, so $X \setminus K$ is open. $\square$

**Theorem.** *Let $X, Y$ be compact and Hausdorff. Then a continuous bijection $f : X \to Y$ is a homeomorphism.*

*Proof.* It suffices to show that $f$ is closed, namely the images of closed sets are closed. Let $A \subset X$ be closed. $A$ is compact, so $f(A) \subset Y$ is compact. But $Y$ is Hausdorff, so this implies $f(A)$ is closed, as desired. $\square$

**Remark.** *The above theorem only requires that $X$ is compact and $Y$ is Hausdorff. However, the conclusion then immediately implies that $X$ and $Y$ are both compact and Hausdorff.*

### Example

- The compactness assumption is really necessary. Consider the bijection

$$\begin{aligned} f : [0, 1) &\to S^1 \\ x &\mapsto e^{2\pi i x} = (\cos(2\pi x), \sin(2\pi x)) \end{aligned}$$

$f$ is a continuous bijection, but not a homeomorphism. One way to see this is that $S^1$ is compact while $[0, 1)$ is not. Alternatively, removing most points from $[0, 1)$ disconnects the space, while removing any point from $S^1$ does not.

Next lecture we will prove the following important result.

**Theorem.** *Let $X$ and $Y$ be compact. Then $X \times Y$ is compact.*$^{22}$

$^{22}$This holds for infinitely, and even uncountably, many compact spaces. This is *Tychonoff's theorem*, and it is equivalent to the axiom of choice.

44

<!-- page 45 -->

# 10/2/2019 - Compactness, Uncountability, Metric Spaces

We will begin by proving the following theorem introduced last lecture.

**Theorem.** Let $X$ and $Y$ be compact. Then $X \times Y$ is compact.

By induction we have the following corollary.

**Corollary.** Let $X_1, \ldots, X_n$ be compact. Then $X_1 \times \ldots X_n$ is compact.

Proof. Let $\mathcal{A}$ be an open cover of $X \times Y$. We want to find a finite subcover of $\mathcal{A}$. A basis element of $X \times Y$ is of the form $U \times V$, where $U \subset X$ and $V \subset Y$ is open. Thus each element of $A$ is the union of such subsets $U \times V$.

The strategy will be to define a new cover that consists of only basis elements and demonstrate that these have a finite subcover. Then by replacing each basis element $U \times V$ with the open set of $\mathcal{A}$ in which it is contained, we obtain a finite subcover of $\mathcal{A}$. This reduces the problem to finding a subcover of a cover that consists of only basis elements, so we can assume that all sets in $\mathcal{A}$ are of the form $U_i \times V_i$, with $U_i \subset X$ and $V_i \subset Y$ open.

Consider a point $x \in X$. $\{x\} \times Y$ is homeomorphic to $Y$ and hence compact. Then it has a finite subcover of the form $\bigcup_{i=1}^n U_i \times V_i$ and $x \in U_i$ for all $i$. If we take the finite intersection $W = \bigcap_{i=1}^n U_i$, then $W$ is an open neighborhood of $x$ in $X$. Also, $\bigcup_{i=1}^n U_i \times V_i$ is a finite cover of $W \times Y$.

![img-9.jpeg](img-9.jpeg)

For every $x$, similarly define an open set $W_x$ to obtain a strip $W_x \times Y$ and a finite subcover of this strip. The sets $W_x$ for all $x$ cover $X$, so by compactness of $X$ there is a finite subcover $W_{x_1}, \ldots, W_{x_m}$. Finitely many sets from $\mathcal{A}$ cover each $W_{x_i} \times Y$, so collecting these all together yields a finite subcover of $\mathcal{A}$ for all of $X \times Y$.

Recall that we proved compact Hausdorff spaces have some nice properties. Namely, if $X$ is Hausdorff and $A \subset X$ is compact, then $A$ is closed. Also, if $f : X \to Y$ is a continuous bijection between compact, Hausdorff spaces $X$ and $Y$ then $f$ is a homeomorphism. We have the following neat application of these ideas.

45

<!-- page 46 -->

### Uncountability of \(\mathbb{R}\)

We first introduce the following definition.

Definition. Let X be a topological space. An isolated point of X is a point  \( x \in X \)  such that the singleton  \( \{x\} \)  is open.

Theorem. If X is a nonempty, compact Hausdorff space with no isolated points, then X is uncountable. \( ^{a} \)

We first need the following lemma.

Lemma. If \( U \subset X \) is open and \( x \in X \), there exists a nonempty open set \( V \) with \( x \notin \overline{V} \) and \( V \subset U \).

Proof. Choose  \( y \in U \)  such that  \( x \neq y \) . This is possible because U is a neighborhood of x and x is not an isolated point. By Hausdorffness, there are disjoint neighborhoods  \( W_x \)  of x and  \( W_y \)  of y. Take  \( V = W_y \cap U \) , which is nonempty as it contains y. Then  \( W_x \)  is open and disjoint from V, so  \( \overline{V} \subset X \setminus W_x \)  and  \( x \notin \overline{V} \) . ☐

We now prove the theorem.

Proof. Let \( f: \mathbb{N} \to X \) be any function. We will show that \( f \) is not a surjection. This will imply that \( X \) is not countable.\(^b\) We will define a sequence of sets by induction. By the claim, set \( U = X \) and find \( V_1 \subset X \) such that \( f(1) \notin \overline{V_1} \). For \( n > 1 \), apply the claim to the point \( f(n) \) and \( U = V_{n-1} \). Then \( \overline{V_1} \supset \overline{V_2} \supset \ldots \) is a sequence of nonempty, closed sets with \( f(n) \notin \overline{V_n} \).

We claim \(\bigcup_{i}(X\setminus \overline{V_i})\neq X\). Suppose for contradiction that we have equality. Then since \(X\) is compact, there is a finite subcover \(X\setminus \overline{V_{i_1}},\ldots ,X\setminus \overline{V_{i_n}}\). But any point in \(\overline{V_j}\) with \(j\) larger than \(i_1,\dots ,i_n\) is not covered by these sets, so this is not actually a cover. Thus \(\bigcap_{i}\overline{V_{i}}\neq \varnothing\).

If we take \( x \in \bigcap_{i} \overline{V}_{i} \), then by definition \( x \neq f(n) \) for any \( n \), and \( f \) is not surjective.

Corollary. Every closed interval of R is uncountable.

\( ^{a} \) This is a special case of general result in topology and functional analysis called the Baire category theorem. Challenge: look up the Baire category theorem on Wikipedia and show that our result follows as a corollary.  \( ^{b} \) A countable set is one that admits a surjection from N by definition.

### Compactness in metric spaces

Recall that  \( A \subset R^{n} \)  is compact if A is closed in bounded. \( ^{23} \)  This agrees with the topological definition.

Theorem. \(A \subset \mathbb{R}^n\) is compact if and only if \(A\) is closed and bounded in the Euclidean metric.

\( ^{23} \) This is the Heine-Borel characterization of compactness in  \( R^{n} \) .

46

<!-- page 47 -->

Proof. Suppose $A \subset \mathbb{R}^n$ is compact. Then $A$ is closed, since $\mathbb{R}^n$ is Hausdorff. Cover $A$ with the open balls $\{B_r(0) : r \in \mathbb{N}\}$. Then by compactness, there is a finite subcover $B_{r_1}(0), \ldots, B_{r_m}(0)$. Then there is some $r$ with $A \subset B_r(0)$, so $A$ is bounded.

Suppose $A \subset \mathbb{R}^n$ is closed and bounded. Since $A$ is bounded, it is contained in some suitably large rectangle $[-r, r]^n$. This closed rectangle is the product of intervals and thus compact. $A$ is a closed subspace of a compact space, so $A$ is compact.

Remark. The theorem depends on the Euclidean metric in an important way. We can define other metrics on $\mathbb{R}^n$ that induce the standard topology, but for which this theorem is not true.

For example, the uniform metric on $\mathbb{R}^n$ induces the same topology as the Euclidean metric, but all of $\mathbb{R}^n$ is bounded in this metric (while $\mathbb{R}^n$ is not compact).

We can use compactness to generalize two of the most important theorems in calculus to compact spaces.

Theorem (Extreme value theorem). If $X$ is compact and $f : X \to \mathbb{R}$ is a continuous function, then $f$ achieves its maximum. Namely, there exists $c \in X$ such that $f(x) \leq f(c)$ for all $x \in X$.

Proof. $f(X) \subset \mathbb{R}$ is compact, so it is bounded and closed (and hence contains its limit points). If $m = \sup(X)$ is in $f(X)$, then we are done. Otherwise, $(m - \epsilon, m) \cap f(X) \neq \varnothing$ for all $\epsilon > 0$ by definition of the supremum, so $m$ is a limit point of $f(X)$ and therefore $m \in f(X)$.

For the next theorem,24 we introduce a few definitions.

Definition. If $(X, d)$ is a metric space and $A \subset X$ is nonempty, the distance from $x \in X$ to $A$ is defined to be $d(x, A) = \inf\{d(x, y) : y \in A\}$.

If $A$ is compact, then there exists a point $y \in A$ with $d(x, y) = d(x, A)$. This is because $d(x, \cdot) : A \to \mathbb{R}$ is a continuous function from a compact set $A$ and achieves its minimum at some point $y \in A$.

Definition. If $A$ is bounded, the diameter of $A$ is defined to be $\sup\{d(x, y) : x, y \in A\}$.

Intuitively, the diameter of $A$ is the largest distance between two points in $A$. If $A$ is compact, then there exist points $x, y \in A$ with $d(x, y)$ equal to the diameter of $A$. This is because $d : A \times A \to \mathbb{R}$ is a continuous function25 from the compact set $A \times A$ to $\mathbb{R}$ and achieves its maximum at some pair $(x, y) \in A \times A$.

The following useful lemma will be essential for the proof.

24Recall that the uniform continuity theorem says that if $f : [a, b] \to \mathbb{R}$ is continuous, then $f$ is uniformly continuous. This means that for any $\epsilon > 0$, there exists $\delta > 0$ such that $|x - y| < \delta$ implies $|f(x) - f(y)| < \epsilon$. In other words, $\delta$ does not depend on the point $x$.

25Verification: $d : A \times A \to \mathbb{R}$ is a continuous function.

47

<!-- page 48 -->

**Lemma.** Let $\mathcal{A}$ be an open cover of a metric space $(X, d)$. If $X$ is compact, then there exists some $\delta > 0$ such that all subsets of $X$ of diameter less than $\delta$ are contained in an element of $\mathcal{A}$. $\delta$ is the **Lebesgue number** of $\mathcal{A}$.

*Proof.* Choose a finite subcover $\{A_1, \ldots, A_n\} \subset \mathcal{A}$. Define the function

$$\begin{array}{l} f: X \to \mathbb{R} \\ x \mapsto \frac{1}{n} \sum_{i=1}^{n} d(x, X \setminus A_i) \end{array}$$

If $x \notin A_i$, then $d(x, X \setminus A_i) = 0$. Intuitively summand measures how far the exterior of $A_i$ is from the point $x$.

$f$ is the sum of continuous functions and is hence continuous. Since each $A_i$ is open, if $x \in A_i$ there is some $\epsilon > 0$ with $x \in B_\epsilon(x) \subset A_i$. Then in such a case, $d(x, X \setminus A_i) > \epsilon$. Any $x \in X$ is contained in some $A_i$, so $f(x) > 0$ for all $x \in X$.

$X$ is compact, so $f$ achieves its minimum $\delta > 0$ with $f(x) \geq \delta$ for all $x \in X$. Then for any $x$, there exists some $A_i$ such that $d(x, X \setminus A_i) \geq \delta$ by definition of $f$ (as $f$ is the average of all $d(x, X \setminus A_i)$). This $\delta$ is the Lebesgue number of $\mathcal{A}$.

We now confirm the result. Suppose $B$ has diameter less than $\delta$. If $x_0 \in B$ then

$$x_0 \in B \subset B_\delta(x_0) \subset A_i$$

We now define uniform continuity.

**Definition.** Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. A function $f: X \to Y$ is **uniformly continuous** if for all $\epsilon > 0$, there exists $\delta > 0$ such that $d_X(x, y) < \delta$ implies $d_Y(f(x), f(y)) < \epsilon$.

We will prove the following theorem next lecture.

**Theorem** (Uniform continuity theorem). If $X$ and $Y$ are metric spaces and $X$ is compact, then any continuous function $f: X \to Y$ is uniformly continuous.

48

<!-- page 49 -->

# 10/7/2019 - Compactness, Limit Points, Sequences

Recall that a space $X$ is compact if every open cover $X = \bigcup_{i \in I} U_i$ has a finite subcover. In $\mathbb{R}^n$ with the usual distance, a subset is compact if and only if it is closed and bounded.

Another useful result is that if $f : X \to Y$ is continuous at $X$ is compact, then $f(X) \subset Y$ is compact. This implies the extreme value theorem for continuous functions $f : X \to \mathbb{R}$, with $X$ compact.

Recall the following useful lemma from last lecture.

Lemma. Let $(X, d)$ be a compact metric space and $\mathcal{A}$ an open cover of $X$. There exists $\delta > 0$ such that any subset of diameter less than $\delta$ is entirely contained in one set of $\mathcal{A}$.

The Lebesgue number lemma is false in noncompact spaces.

### Failure of the Lebesgue lemma for noncompact spaces

- For example, we can cover the noncompact space $\mathbb{R}$ by

$$\bigcup_{n \in \mathbb{Z}} \left( n - (1 + 1/n), n + (1 + 1/n) \right)$$

Then for any $\delta$, we can find a set of radius less than $\delta$ containing some integer that does not lie in a single

- This fails even when we have a finite cover of a noncompact space. For example, $\mathbb{R}^2$ is covered by the two sets

$$A_1 = \{(x, y) : xy < 1\} \cup \{(x, y) : x \le 0 \text{ or } y \le 0\}$$

$$A_2 = \{(x, y) : y > 0\}$$

We can find arbitrarily small balls near the $x$-axis far away that do not sit entirely in one of the two open sets.

Uniform continuity expresses the idea that the neighborhoods of points in the preimages of open sets are 'uniformly sized.' To compare the sizes of neighborhoods, we require a metric on the space.

Definition. A function of metric spaces $f : (X, d_X) \to (Y, d_Y)$ is uniformly continuous if for all $\epsilon > 0$, there exists $\delta > 0$ such that for $x_0, x_1 \in X$ we have $d(x_0, x_1) < \delta$ implies $d(f(x_0), f(x_1)) < \epsilon$.

Theorem. Let $X, Y$ be metric spaces and $f : X \to Y$ a continuous function. If $X$ is compact, then $f$ is uniformly continuous.

We will prove this easily with the Lebesgue number lemma, but there are more complicated proofs that rely directly on the finiteness condition from the definition of compactness.

49

<!-- page 50 -->

Proof. Given $\epsilon > 0$, consider the cover of $Y$ given by taking all balls of radius $\epsilon/2$. The idea will be that if we guarantee $f(x_0)$ and $f(x_1)$ are in the same ball, then the distance between them is less than $\epsilon$ by the triangle inequality.

Take the open cover

$$X = \bigcup_{y \in Y} f^{-1}(B_{\epsilon/2}(y))$$

By the Lebesgue number lemma, there exists some $\delta > 0$ such that if $d_X(x_0, x_1) < \delta$ implies that $x_0, x_1 \in f^{-1}(B_{\epsilon/2}(y))$ for some $y \in Y$. Therefore $f(x_0), f(x_1) \in B_{\epsilon/2}(y)$ and $d_Y(f(x_0), f(x_1)) < \epsilon$.

### Limit point and sequential compactness

There are two other definitions of compactness. In a metric space, these notions coincide, but they differ in a general topological space. The reason for this is that sequences do not capture the topological information of a general space very well.

Definition. A space $X$ is limit point compact if every infinite subset of $X$ has a limit point.

Examples]

- $(0, 1] \subset \mathbb{R}$ is not limit point compact, as the infinite collection $\{1/n : n \in \mathbb{N}\}$ has no limit point in $(0, 1]$.
- $\mathbb{R}$ is not limit point compact, as $\mathbb{Z} \subset \mathbb{R}$ is an infinite subset with no limit point.
- $\{1/n : n \in \mathbb{N}\} \cup \{0\}$ is limit point compact. Any infinite subset has 0 as a limit point necessarily.

So far limit point compactness seems to agree with the usual definition.

Theorem. Let $X$ be compact. Then $X$ is limit point compact.

Proof. We will show the contrapositive. Suppose $X$ is not limit point compact, and let $A \subset X$ be an infinite subset with no limit point. For each $a \in A$, $a$ is not a limit point of $A$, and thus there exists a neighborhood $U_a$ of $a$ such that $U_a \cap A = \{a\}$.

We have constructed a cover of $A$, so it remains to cover the rest of $X$. $A$ has no limit points, so it is closed. Thus $X \setminus A$ is open, which yields an open cover

$$X = (X \setminus A) \cup \bigcup_{a \in A} U_a$$

This is an open cover with no finite subcover, as $a \in U_a$ and no other sets in this cover. Therefore $X$ is not compact.

50

<!-- page 51 -->

The easiest counterexamples to the converse are non-Hausdorff, but it is possible to define a Hausdorff counterexample as well (although it may be a bit more complicated).

### Failure of the converse

- Consider $\mathbb{Z}$ with the topology generated by the sets of the form $\{-n, n\}$ for all $n \in \mathbb{Z}$ along with $\{0\}$. $\mathbb{Z}$ is not Hausdorff, as it is not possible to separate the points $-n$ and $n$.

Given an infinite subset $S \subset \mathbb{Z}$, let $n \in S \setminus \{0\}$. The claim is that $-n$ is a limit point, as every neighborhood of $-n$ contains $n$, an element of $S$ distinct from $-n$.

There is another notion of compactness as well.

Definition. $X$ is sequentially compact if every sequence of points in $X$ has a convergent subsequence.

### Example

- In $\mathbb{R}$, every bounded sequence in $[-R, R]$ has a convergent subsequence.

For example, $1, 0, 1, 0, \ldots$ has a convergent subsequence $1, 1, \ldots$.

- The sequence $1, 2, 3, \ldots$ in $\mathbb{R}$ has no convergent subsequence, even though the sequence $1, 1/2, 2, 1/3, 3, \ldots$ has a convergent subsequence $1, 1/2, 1/3, \ldots$.

It is natural to ask how sequential compactness relates to limit point compactness and usual compactness. In spaces with a countable basis of neighborhoods (for example metric spaces), the notion of a limit of a sequence is closely related to that of the limit point of a set. In such a case, sequentially compactness is equivalent to limit point compactness.

In general, however, sequentially compactness only implies limit point compactness. This should be understood as a failure for sequences to detect the topology of a space rather than a reflection of the strength of these competing notions.26 We will prove the following important characterization of these notions.

Theorem. If $(X, d)$ is a metric space, then compactness, limit point compactness, and sequential compactness are equivalent.

Proof. We showed compactness implies limit point compactness already. Let $X$ be limit point compact, and let $x_1, x_2, \ldots$ be a sequence in $X$. If this sequence consists of only finitely many distinct terms, then there exists some $a = x_i$ that reappears infinitely many times in the sequence. Namely, $x_n = a$ for infinitely many $n$. These indices form a convergent subsequence.

Otherwise, the infinite set $\{x_1, x_2, \ldots\}$ has a limit point $a \in X$ by assumption. Let $n_1$ be such

26There is a generalization of a sequence called a net that is designed to capture the topology of a space that doesn't admit such a countable description.

51

<!-- page 52 -->

that $x_{n_1} \in B_1(a)$. Then inductively take $n_i > n_{i-1}$ with $x_{n_i} \in B_{1/i}(a)$. This yields a subsequence converging to $a$.

Let $X$ be sequentially compact. We introduce the following lemma.

**Lemma.** *If $X$ is sequentially compact, then for all $\epsilon > 0$, $X$ can be covered by finitely many open balls of radius $\epsilon$.*

*Proof.* Suppose for contradiction there exists $\epsilon > 0$ such that no finite collection of balls of radius $\epsilon$ cover $X$. Take $x_1 \in X$, and inductively take $x_n \in X \setminus \bigcup_{i=1}^n B_\epsilon(x_i)$. Thus we have a sequence $x_1, x_2, \ldots, x_n$ with distance between any distinct points at least $\epsilon$. This yields a sequence with no convergent subsequence, which is a contradiction. $\square$

We will also need the next lemma.

**Lemma.** *Let $X$ be sequentially compact. Then every open cover of $X$ has a Lebesgue number.*

*Proof.* Suppose for contradiction$^{27}$ there is a cover $\mathcal{A} = \{A_i\}_{i \in I}$. For all $n$, there exists $C_n \subset X$ with diameter less than $1/n$ such that $C_n$ is not contained in any single $A_i$.

Choose $x_n \in C_n$ for all $n$. By sequential compactness, there exists a convergent subsequence that converges to some $a$. We know $a \in A_i$ for some $i$, and thus there exists $\epsilon > 0$ with $a \in B_\epsilon(a) \subset A_i$. Pick $k$ large enough so that $d(x_{n_k}, a) < \epsilon/2$. Then the diameter of $C_{n_k}$ is less than $1/n_k < \epsilon/2$. This implies

$$C_{n_k} \subset B_{\epsilon/2}(x_{n_k}) \subset B_\epsilon(a) \subset A_i$$

which is a contradiction. $\square$

It is now easy to prove the last part of the theorem. For sequentially compact $X$, given an open cover $X = \bigcup_{i \in I} U_i$, by the second lemma there exists $\delta > 0$ such that every subset of diameter less than $\delta$ is contained entirely in some $U_i$. Let $\epsilon < \delta/2$. Then by the first lemma $X$ can be covered by finitely many balls $B_\epsilon(x_1), \ldots, B_\epsilon(x_n)$, where $B_\epsilon(x_i) \subset U_{j_i}$. Thus $U_{j_1}, \ldots, U_{j_n}$ are a finite subcover, and $X$ is compact. $\square$

$^{27}$In general it is easier to contradict sequential compactness by building a sequence with no convergent subsequence than to try leverage this condition to prove the claim directly.

52

<!-- page 53 -->

# 10/9/2019 - Compactifications and Local Compactness

We saw on the homework assignment that although \(\mathbb{R}^n\) is not compact, \(\mathbb{R}^n\cup \{\infty \}\) with a basis given by the usual open balls along with

\[
U _ {r} = \{x \in \mathbb {R} ^ {n}: | x | > r \} \cup \{\infty \}
\]

for \( r > 0 \) is compact. This is a case of a more general construction, the compactification of a space.

Definition. Let Y be compact and Hausdorff. If  \( X \hookrightarrow Y \)  is an embedding \( ^{28} \)  such that X is dense in Y, then Y is a compactification of X. If  \( Y \setminus X \)  is a single point, then Y is the one-point compactification of X.

# Examples

- The circle \( S^1 \) is a compactification of the open interval \( (0,1) \). However, \( [0,1] \) is also a compactification of \( (0,1) \), which shows that compactifications are not necessarily unique.
- The open square \((0,1) \times (0,1)\) has many compactifications:
  - The closed square \([0,1] \times [0,1]\) is a compactification.
  - The sphere \( S^2 \) is a compactification (the one-point compactification, as \( (0,1) \times (0,1) \) is homeomorphic to \( \mathbb{R}^2 \)).
  - The torus \( S^1 \times S^1 \) is a compactification.
- Real or complex projective space \((\mathbb{R}P^n\) or \(\mathbb{C}P^n)\) is a compactification of \(\mathbb{R}^n\) or \(\mathbb{C}^n\).
- Let \(\mathbb{Z}\) be endowed with the discrete topology and take \(X = \mathbb{Z} \cup \{\infty\}\), given the subspace topology in \(\mathbb{R} \cup \{\infty\}\). Then \(X\) is the one-point compactification of \(\mathbb{Z}\).

Compactifications are very useful. For example, in algebraic geometry compact varieties are much easier to work with. It is thus worth investigation when they exist, and what sort of properties they exhibit. To answer this question, we introduce local compactness.

Definition. A space \( X \) is locally compact at \( x \) if there exists a compact subset \( K \subset X \) which contains a neighborhood of \( x \). \( X \) is locally compact if it is locally compact at all \( x \in X \).

# Examples

- Any compact space is locally compact.
- \(\mathbb{R}^n\) is locally compact. For all points \(x \in \mathbb{R}^n\), the closed ball \(\overline{B_r(x)}\) is a closed and bounded subset of \(\mathbb{R}^n\) (thus compact) that contains the open neighborhood \(B_r(x)\).
- \(\mathbb{R}^{\omega}\) with the product topology is not locally compact, as none of its basis elements are contained in compact subspaces (otherwise their closures would be a closed subset of a compact space and hence compact). More explicitly, local compactness at 0 would require

\( ^{28} \) An embedding is a homeomorphism onto its image. Intuitively, an embedding allows us to view the abstract topological space X as a subspace of Y.

53

<!-- page 54 -->

some neighborhood

$$(-\epsilon, \epsilon) \times \dots \times (-\epsilon, \epsilon) \times \mathbb{R} \times \mathbb{R} \times \dots$$

to lie in a compact neighborhood, which implies

$$[-\epsilon, \epsilon] \times \dots \times [-\epsilon, \epsilon] \times \mathbb{R} \times \mathbb{R} \times \dots$$

is compact. But this is easily seen to be a contradiction.

## Constructing compactifications

Local compactness turns out to be precisely the assumption both necessary and sufficient to ensure that a Hausdorff space $X$ has a Hausdorff one-point compactification.

**Theorem.** $X$ is a locally compact Hausdorff space if and only if there exists a one-point compactification $Y$ of $X$. Moreover, if such a compactification $Y$ exists, then it is unique up to homeomorphism.

*Proof.* Suppose $Y = X \cup \{\infty\}$ is a one-point compactification, namely that it is compact and Hausdorff. The subspace $X \subset Y$ is Hausdorff, and if $x \in X$ choose disjoint neighborhoods $x \in U$ and $\infty \in V$. Let $C = Y \setminus V$. $C$ is compact, as it is a closed subspace of $Y$. And

$$x \in U \subset C = Y \setminus V \subset Y \setminus \{\infty\} = X$$

Therefore $Y$ is locally compact at $x$.

Suppose $X$ is locally compact Hausdorff. Define $Y$ as the set $Y = X \cup \{\infty\}$, where the element $\infty \notin X$ is a distinct symbol. Define a topology on $Y$ by

$$\mathcal{T} = \underbrace{\{U : U \subset X \text{ open}\}}_{(1)} \cup \underbrace{\{Y \setminus C : C \subset X \text{ compact}\}}_{(2)}$$

The first sets (1) are those that are already open in $X$. The second sets (2) are those containing $\infty$ whose complements are compact subsets of $X$.

1. We first confirm that this indeed defines a topology. The empty set $\varnothing$ is in the first summand (1). The space $Y = Y \setminus \varnothing$ is in the second summand (2).

Arbitrary unions and finite intersections of type (1) are of type (1), and the unions and intersections of type (2) are type (2). This is because if $C_i \subset X$ is a collection of compact subspaces for $i \in I$, then $\bigcap_{i \in I}$ is compact and $C_1 \cup \ldots \cup C_n$ is compact.$^{29}$

If $U \subset X$ is open and $C \subset X$ is compact (and hence closed), then

$$U \cap (Y \setminus C) = U \cap (X \setminus C)$$

is open of type (1) and

$$U \cup (Y \setminus C) = Y \setminus (C \cap (X \setminus U))$$

$^{29}$These claims are not too difficult to prove.

54

<!-- page 55 -->

is open of type (2), as $C \cap (X \setminus U)$ is closed in $C$ and hence compact.

Moreover, since $X$ is open in $Y$, as it is of type (1), the subspace topology on $X$ induced by $\mathcal{T}$ is the original topology on $X$.

2. $Y$ is Hausdorff. If two points $x, y \in Y$ lie in $X$, then they can be separated by the corresponding open neighborhoods that arise from the Hausdorff $X \subset Y$. To separate $x \in X$ and $\infty$, local compactness implies there exists a compact $C$ containing an open neighborhood $U$ of $x$. Then $U$ and $Y \setminus C$ separate $x$ and $\infty$.

3. $Y$ is compact. Let $\{U_i\}_{i \in I}$ be an open cover. $\infty$ lies in some $U_0 = Y \setminus C$, for $C$ compact. Now $\{U_i \cap C\}_{i \in I}$ are an open cover of $C$, so by compactness there exists a finite subcover $C = (U_1 \cap C) \cup \ldots \cup (U_n \cap C)$. Thus $C \subset U_1 \cup \ldots \cup U_n$, and $Y = U_0 \cup U_1 \cup \ldots \cup U_n$.

4. Finally, $Y$ is unique up to homeomorphism. Suppose there is another $Y' = X \cup \{p\}$ that is compact and Hausdorff such that subspace topology on $X$ agrees with our original topology on $X$. We will show that the map $Y \to Y'$ defined by the identity on $X$ and $\infty \mapsto p$ is a homeomorphism, so that the only difference between $Y$ and $Y'$ is the naming of the added point.

- $\{p\}$ is closed, as $Y'$ is Hausdorff. Therefore $X \subset Y'$ is open. So the subspace topology on $X$ consists exactly of open subsets of $Y'$ which contain $X$. Then the type (1) open sets in $Y'$ are exactly the open sets of $X$.
- If $V \subset Y'$ is open and $p \in V$, then $C = Y' \setminus V$ is closed in $Y'$, and hence $C$ is compact. But in fact $C \subset Y' \setminus \{p\} = X$, so $V = Y' \setminus C$, where $C \subset X$, is compact. Conversely, if $C \subset X$ is compact, then it is closed in $Y'$ by Hausdorffness, and so $Y' \setminus C$ must be open in $Y'$.

Note that the definition we have given for local compactness doesn't seem very local.$^{30}$ We can provide a better formulation when $X$ is Hausdorff.

**Proposition.** Assume $X$ is Hausdorff. Then $X$ is locally compact if and only if for all $x \in X$ and neighborhoods $U$ of $x$, there exists a neighborhood $V$ of $x$ such that $\overline{V} \subset U$ and $\overline{V}$ is compact.

Proof. Suppose for all $x \in X$ and neighborhoods $U$ of $x$, there exists a neighborhood $V$ of $x$ such that $\overline{V} \subset U$ and $\overline{V}$ is compact. Take $U = X$, at which points there exists compact $\overline{V}$ containing $x$ that contains the open neighborhood $V$ of $x$.

Now suppose $X$ is locally compact. Let $x \in X$ and $U$ be a neighborhood of $x$. Let $Y$ be the one-point compactification of $X$. Recall that $Y$ is compact Hausdorff and $C = Y \setminus U$ is closed in $Y$ and thus compact. We require the following lemma.

**Lemma.** Let $Y$ be Hausdorff. If $C \subset Y$ is compact and disjoint from $x$, then there exist disjoint open neighborhoods $V$ of $x$ and $V'$ of $C$.

$^{30}$The term *local* in topology usually means something like examining arbitrarily small neighborhoods.

55

<!-- page 56 -->

Proof. The proof of this lemma just like proof that compact sets in a Hausdorff space are closed. Since $x \notin C$, for each $y \in C$ we can choose disjoint open neighborhoods $V_y$ of $x$ and $V'_y$ of $y$. The collection $\{V'_y\}_{y \in C}$ is a cover of $C$, and by compactness thus admits a finite subcover $V'_{y_1}, \ldots, V'_{y_n}$. Then take $V = V_{y_1} \cap \ldots \cap V_{y_n}$ and $V' = V'_{y_1} \cup \ldots \cup V'_{y_n}$. $V$ does not intersect any $V'_{y_i}$, so $V \cap V' = \varnothing$. And $x \in V$ and $C \subset V'$, as desired.

Apply the lemma to conclude that there exists disjoint neighborhoods $V$ around $x$ and $V'$ around $Y \setminus U$. Thus we have

$$x \in V \subset \overline{V} \subset (Y \setminus V') \subset (Y \setminus C = U)$$

Next time we will introduce *separation axioms*, which are a similar way of describe to what extend points and subsets of a topological space can be separated by open sets. We will focus on *normal spaces* and *metrizability*.

56

<!-- page 57 -->

# 10/16/2019 - Countability, Separability, and Normal Spaces

We will speak a bit about separation axioms and metrizability. One could discuss point set topology for a long time, but we will limit ourselves to a brief overview of the subject.31

## Countability

There are different ways in which a topological space can be ‘countably complicated’. We are of course not demanding that the underlying set be countable or the topology of open sets be countable.

Definition. A topological space X has a countable basis of neighborhoods at x ∈ X if there exists a countable collection U1, U2, … of neighborhoods of x such that every neighborhood V of x contains some Ui.

This captures the idea that a topological space could have countable complexity locally.

Definition. A space with a countable basis of neighborhoods at all x ∈ X is first countable.

### Examples

- Any metric space is first countable. For each x ∈ X, take Un = B1/n(x). Then U1, U2, … is a countable basis of neighborhoods at x.
- Rℓ is first countable. Take Un = [x, x + 1/n).

First countability is a way of characterizing when sequences are capable of detecting topological phenomena.

Theorem. Let A ⊂ X be a subspace, and let x ∈ X. If there exists a sequence (an) with an ∈ A that converges to x, then x ∈ A̅. If X is first countable, then the converse also holds.

We can assume that the basis of neighborhoods satisfies a descending chain U1 ⊃ U2 ⊃ …. Then take an ∈ Un to obtain a sequence that converges to a.

There is a stronger notion of countability on a topological space as well.

Definition. A topological space X is second countable if its topology admits a countable basis.

### Example

- ℝ with the usual topology is second countable, as the basis {(a, b) : a, b ∈ ℚ} generates the Euclidean topology.
- ℝⁿ with the usual topology is second countable, as the basis {(a1, b1) × … × (an, bn) : ai, bi ∈ ℚ} generates the Euclidean topology.
- ℝ⊥ with the product topology is second countable, as it is generated by products of ℝ

31Lots of additional point set topology comes up in functional analysis.

57

<!-- page 58 -->

with finitely many open intervals with rational endpoints. This is because the set of all finite subsets of a countable set is itself countable.

- •  $\mathbb{R}^\omega$  with the uniform topology is not second countable, even though it is a metric space. Indeed,  $\{0, 1\}^\omega \subset \mathbb{R}^\omega$  is an uncountable subset that is discrete in the uniform topology. Thus there exist basis elements  $B_{r_x}(x)$  around each  $x \in \{0, 1\}^\omega$  that does not intersect any other points of  $\{0, 1\}^\omega$ . This implies that any basis of  $\mathbb{R}^\omega$  with the uniform topology is uncountable.$^a$

$^a$Note that  $\mathbb{R}^\omega$  with the uniform topology is still first countable.

**Proposition.** *If $X$ is second countable, then $X$ contains a countable, dense subset.*

*Proof.* Given a countable basis, choose a point from each nonempty element of the basis. Every open set must contain a basis element and hence one of these points. $\square$

The converse of this proposition is not true.  $\mathbb{R}_\ell$  has a dense, countable subset  $\mathbb{Q}$ . The idea is that we must include half-open intervals that begin at every irrational number, and there are uncountably many such irrationals.

### Regular and normal spaces

Recall that a space $X$ is Hausdorff if distinct points have disjoint, open neighborhoods. This implies the weaker property that single points are closed.

**Definition.** *Suppose the singletons $\{x\} \subset X$ are closed for all $x \in X$.*

*$X$ is **regular** if, for all $x \in X$ and closed subsets $B \subset X$ disjoint from $x$, there exist disjoint, open $U, V \subset X$ with $x \in U$ and $B \subset V$.*

*$X$ is **normal** if for all disjoint, closed $A, B \subset X$ there exist disjoint, open $U, V \subset X$ with $A \subset U$ and $B \subset V$.*

If a space is normal, it is regular (we can take the closed set $A$ simply to be $\{x\}$). If a space is regular, it is Hausdorff (we can take the closet set $B$ simply to be $\{y\}$).

Many common spaces are normal, but it is useful to examine carefully the boundaries between them.

### Example

- •  $\mathbb{R}_\ell$  is normal. Let  $A, B \subset \mathbb{R}_\ell$  be disjoint and closed. Given a point  $a \in A$ , there exists a neighborhood of  $a$  disjoint from the closed set  $B$ . Namely,  $[a, a + \epsilon_a) \cap B = \varnothing$  for some  $\epsilon_a > 0$ . Similarly, there is an open neighborhood  $[b, b + \epsilon_a)$  of  $b$  that is disjoint from  $A$ .

Let  $U = \bigcup_{a \in A} [a, a + \epsilon_a)$  and  $V = \bigcup_{b \in B} [b, b + \epsilon_b)$ .  $U$  and  $V$  are open. They remain disjoint, as we expand both sets to right (and they will not intersect, as we do not increase them to the left).

58

<!-- page 59 -->

- Normality is not necessarily preserved over products. $\mathbb{R}_t^2$ is regular, as the product of regular spaces is regular. However, the product is not normal (this is one of the simplest examples of the failure of normality over products).$^a$
- $\mathbb{R}$ and $\mathbb{R}^n$ are normal. In fact, $\mathbb{R}^\omega$ with the product or the uniform topology is also normal. If $\mathfrak{I}$ is uncountable, then $\mathbb{R}^\mathfrak{I}$ is regular but not normal.

$^a$The proof is quite involved.

**Theorem.** *If $X$ is a regular space with a countable basis, then $X$ is normal.*

The idea of the proof is that given two closed sets, we use the countable basis to provide an order by which we build up the two open neighborhoods. We have the following consequential theorem.

**Theorem.** *Every metric space is normal.*

*Proof.* Let $A, B$ be disjoint, closed sets in $X$. For all $a \in A$, there exists $\epsilon_a > 0$ such that $B(a, \epsilon_a) \cap B = \varnothing$. Similarly, for all $b \in B$ there exists $\epsilon_b > 0$ such that $B(b, \epsilon_b) \cap A = \varnothing$. Let

$$U = \bigcup_{a \in A} B\left(a, \frac{\epsilon_a}{2}\right)$$

$$V = \bigcup_{b \in B} B\left(b, \frac{\epsilon_b}{2}\right)$$

The claim is that $U \cap V = \varnothing$. Indeed, if $z \in U \cap V$ there exists $a \in A$ and $b \in B$ such that $d(a, z) < \epsilon_a/2$ and $d(b, z) < \epsilon_b/2$. By the triangle inequality

$$d(a, b) \le d(a, z) + d(z, b) < \frac{\epsilon_a}{2} + \frac{\epsilon_b}{2} \le \max\{\epsilon_a, \epsilon_b\}$$

which implies $z \in B(a, \epsilon_a)$ or $z \in B(b, \epsilon_b)$.

**Theorem.** *Every compact Hausdorff space is normal.*

*Proof.* Let $x \in X$ and $B \subset X$ be closed (and thus compact). If $x \notin B$, given any point $y \in B$ there exist disjoint, open $U_y, V_y$ with $x \in U_y$ and $y \in V_y$ by Hausdorffness. By compactness, there exist $y_1, \ldots, y_n$ with $B \subset \bigcup_{i=1}^n V_{y_i}$. Take $U = \bigcap_{i=1}^n U_{y_i}$. $U, V$ are open and disjoint, so $X$ is regular.

Given closed (and thus compact), disjoint $A, B \subset X$, for all $y \in B$ there exist disjoint, open $U_y, V_y$ with $A \subset U_y$ and $y \in V_y$. $B$ is compact, so there exist $y_1, \ldots, y_n$ with $B \subset \bigcup_{i=1}^n V_{y_1}$. Take $U = \bigcap_{i=1}^n U_{y_1}$ and $V = \bigcup_{i=1}^n V_{y_i}$. Then $U \cap V = \varnothing$, so $X$ is normal.

We know a metric space is regular and normal. The *Urysohn metrization theorem* provides a converse.

**Theorem.** *Let $X$ be regular with a countable basis. Then $X$ is metrizable.*

The first condition is necessary, but the second one is not optimal. The *Nagata-Smirnov metrization theorem* weakens this assumption.

59

<!-- page 60 -->

**Theorem.** *X is metrizable if and only if X is regular and admits a countable, locally-finite basis.*$^{32}$

We will not both to prove this stronger version, but the proof of the Urysohn metrization lemma has an elegant proof. The key idea will be to build continuous functions that separate closed subsets.

$^{32}$This is a basis that is a union of countably many components, each of which is locally finite (this means there exists a neighborhood of every point in the space that intersects only finitely many of these components).

60

<!-- page 61 -->

# 10/21/2019 - Urysohn's Lemma and the Metrization Theorem

The following result is the Urysohn metrization theorem.

**Theorem.** If $X$ is regular$^{33}$ and has a countable basis, then $X$ is metrizable.

The key ingredient in this theorem is Urysohn's lemma.

**Theorem.** Let $X$ be a normal space and $A, B$ be disjoint closed subsets. Then there exists a continuous function $f : X \to [0, 1]$ such that $f(x) = 0$ for all $x \in A$ and $f(x) = 1$ for all $x \in B$.

The idea of the proof will first be to construct open sets $U_q$ for all $q \in [0, 1] \cap \mathbb{Q}$ such that

$$A \subset U_0 \subset \dots \subset U_1 = X \setminus B$$

and $p < q$ implies $\overline{U}_p \subset U_q$, suing normality of $X$. The second step will be to define

$$f(x) = \inf\{q \in \mathbb{Q} : x \in U_q\}$$

and show that $f$ is continuous.

The first step will use the following formulation of normality.

**Lemma.** If $X$ is normal, then for all closed $A \subset X$ and open $U \supset A$, there exists an open $V \subset X$ such that $A \subset V$ and $\overline{V} \subset U$.

Intuitively, this says that in a normal space every neighborhood of a closed subset contains another smaller open neighborhood and its closure.

Proof. $A$ and $B = X \setminus U$ are disjoint closed sets, so by normality there exist disjoint open $V \supset A$ and $V' \supset B$. $X \setminus V'$ is closed, so $V \subset X \setminus V'$ implies $\overline{V} \subset X \setminus V'$. We have

$$A \subset V \subset \overline{V} \subset (X \setminus V') \subset (X \setminus B = U)$$

as desired.

We now present a proof of Urysohn's lemma.

Proof. We begin with the first step outlined above. Let $A, B$ be disjoint and closed. Take $U_1 = X \setminus B$, and by the previous lemma let $U_0$ be open such that $A \subset U_0 \subset \overline{U_0} \subset U_1$. Next, we construct $U_q$ for $q \in (0, 1) \cap \mathbb{Q}$ such that $p < q$ implies $\overline{U_p} \subset U_q$. This proceeds by induction. Choose a well

$^{33}$Recall that this means it is possible to separate points from closed sets. Namely, if $x$ is disjoint from a closed set $A$ then there exists disjoint open neighborhoods $U$ of $x$ and $V$ of $A$. However, a regular space that admits a countable basis is normal, which means that it is possible to separate disjoint closed sets from each other.

61

<!-- page 62 -->

ordering$^{34}$ $\{q_0, q_1, q_2, \ldots\}$ of $[0, 1] \cap \mathbb{Q}$ such that $q_0 = 0$ and $q_1 = 1$. Assuming $U_{q_0}, \ldots, U_{q_n}$ have already been chosen we construct $U_{q_{n+1}}$ using the above lemma. Namely, take

$$q_k = \max \left( \{q_0, \ldots, q_n\} \cap [0, q_{n+1}) \right)$$

$$q_\ell = \min \left( \{q_0, \ldots, q_n\} \cap (q_{n+1}, 1] \right)$$

so that $q_k < q_{n+1} < q_\ell$ and none of the rationals already consider lie in between these. By the inductive hypothesis, $\overline{U_{q_k}} \subset U_{q_\ell}$, so by using normality there exists an open set $V$ such that $\overline{U_{q_k}} \subset V \subset \overline{V} \subset V_{q_\ell}$. Let $U_{q_{n+1}} = V$. Also set $U_q = \varnothing$ for $q < 0$ and $V_q = X$ for $q > 1$, and observe that we have a collection $\{U_q\}_{q \in \mathbb{Q}}$ such that $p < q$ implies $\overline{U_p} \subset U_q$.

Next, define the function

$$f(x) = \inf Q_x$$

where

$$Q_x = \{q \in \mathbb{Q} : x \in U_q\}$$

We have that $f$ satisfies the following properties.

- $f(x) \le 1$ for all $x \in X$ since $x \in U_q$ for all $q > 1$.
- If $x \in B$ then $x \notin U_1 = X \setminus B$, so $Q_x = \mathbb{Q} \cap (1, \infty)$ and $f(x) = 1$.
- $f(x) \ge 0$ for all $x \in X$ since $Q_x \subset [0, \infty)$ because $U_q = \varnothing$ when $q < 0$.
- If $x \in A \subset U_0$, then $0 \in Q_x$ and $f(x) = 0$.

So the function $f$ satisfies the desired properties, and it only remains to show that $f$ is continuous.

- $x \in \overline{U_q}$ implies $f(x) \le q$. If $x \in \overline{U_q}$ then $x \in U_{q'}$ for all $q' > q$, so $Q_x \supset \mathbb{Q} \cap (q, \infty)$.
- $x \notin U_q$ implies $f(x) \ge q$. If $x \notin U_q$ then $Q_x \subset \mathbb{Q} \cap (q, \infty)$.

Now we can prove that $f^{-1}((c, d))$ is open in $X$ for all open intervals $(c, d)$. Assume $x_0 \in f^{-1}((c, d))$, and let $p, q \in \mathbb{Q}$ such that $c < p < f(x_0) < q < d$. Then by the above remarks, $x_0 \in U_q$ and $x_0 \notin \overline{U_p}$. The set $V = U_q \cap (X \setminus \overline{U_p})$ is open and a neighborhood of $x_0$. Moreover, $x \in V$ implies $x \notin U_p$ so $f(x) \ge p$ and $x \in \overline{U_q}$ so $f(x) \le q$. Therefore $V \subset f^{-1}((c, d))$, which completes the proof.

Now we can prove the metrization theorem. We will do this by embedding $X$ into a metric space, namely $[0, 1]^\omega$ with either the product topology or the uniform topology. The uniform topology comes from the metric

$$d_\infty((x_n), (y_n)) = \sup\{|y_n - x_n|\}$$

and the product topology comes from the metric

$$d'_\infty((x_n), (y_n)) = \sup \left\{ \frac{1}{n} |y_n - x_n| \right\}$$

$^{34}$A well ordering is a total ordering $<$ on $(0, 1) \cap \mathbb{Q}$, namely an irreflexive, antisymmetric, transitive, total relation that is wellfounded, which means every nonempty subset contains a least element. This allows us to induct over the rationals, and the existence of such a well-ordering on any set is equivalent to the axiom of choice.

62

<!-- page 63 -->

The balls in the metric $d'_{\infty}$ are

$$B_{\epsilon}^{d'_{\infty}}((x_n)) = \prod_n(x_n - n\epsilon, x_n + n\epsilon)$$

The key point is that for $n > \epsilon^{-1}$ the multiplicand $(x_n - n\epsilon, x_n + n\epsilon)$ is all of $[0, 1]$. We require the following lemma.

**Lemma.** *There exists a countable collection of continuous functions $f_n : X \to [0, 1]$ such that for all $x_0 \in X$ and neighborhoods $U$ of $x_0$, there exists $n$ for which $f_n(x_0) > 0$ and $f_n = 0$ on $X \setminus U$.*

*Proof.* This follows from Urysohn's lemma, but we need to be careful to ensure that countably many functions suffices. Let $B = \{B_n\}$ be a countable basis for $X$. If $U$ is an open neighborhood of $x_0$ then there exists some $B_n$ such that $x_0 \in B_n \subset U$. By normality of $X$, there exists open $V$ for which $x \in V \subset \overline{V} \subset B_n$ and there exists $B_m$ such that $x \in B_m \subset V$. This yields $x \in \overline{B_m} \subset B_n \subset U$.

For every $(m, n) \in \mathbb{N} \times \mathbb{N}$ such that $\overline{B_m} \subset B_n$, apply Urysohn's lemma to obtain a function $g_{m,n} : X \to [0, 1]$ such that $g_{m,n} = 1$ on $\overline{B_m}$ and $g_{m,n} = 0$ on $X \setminus B_n$. This yields a countable collection of functions $\{g_{m,n} : m, n \in \mathbb{N}\}$ with the desired property.

We can now prove the theorem.

*Proof.* Let $\{f_n : n \in \mathbb{N}\}$ be a countable collection of functions as in the lemma. The claim is that

$$\begin{array}{l} F : X \to [0, 1]^\omega \\ x \mapsto (f_1(x), f_2(x), \dots) \end{array}$$

is an embedding, which shows that the topology on $X$ can be obtained by restricting the $d'_{\infty}$ metric from $[0, 1]^\omega$.

- $F$ is continuous in the product topology because each component $f_n$ is continuous by construction.
- $F$ is injective, since $x \neq y$ implies there exists disjoint neighborhoods $U$ of $x$ and $V$ of $y$. Thus there exists $m, n \in \mathbb{N}$ such that $f_n(x) > 0$ and $f_n = 0$ outside of $U$ (at $y$) and $f_m(y) > 0$ and $f_m = 0$ outside of $V$ (hence at $x$).
- $F$ defines a continuous bijection onto its image $Z = F(X)$, it only remains to show that if $U \subset X$ is open then $F(U) \subset Z$ is open. For this, let $U \subset X$ be open and $x_0 \in U$. Then there exists $n$ such that $f_n(x_0) > 0$ and $f_n = 0$ outside of $U$. Let

$$V_n = \pi_n^{-1}((0, \infty)) \cap Z = \{(z_1, z_2, \dots) \in Z : z_n > 0\} \subset Z$$

$V_n$ is open. Then $x_0 \in F^{-1}(V_n) \subset U$, since $f_n(x_0) > 0$ and $f_n(x) > 0$ implies $x \in U$. Therefore $F(x_0) \in V_n \subset F(U)$, with $V_n$ open in $Z$. This holds for all $x_0 \in U$, so we conclude $F(U)$ is open.

Therefore $F : X \to Z$ is a homeomorphism, and $X$ is in fact a metric space.

**Remark.** *When $X$ does not admit a countable basis this procedure still produces embeddings of $X$ into $[0, 1]^I$. However, $[0, 1]^I$ is not metrizable when $I$ is uncountable.*

63

<!-- page 64 -->

# 10/23/2019 - Category Theory, Paths, Homotopy

Today we will begin the second part of the course, which is an introduction to *algebraic topology*.

## Categories

*Category theory* is a language that provides a precise way to formulate patterns that appear in different areas of mathematics.

**Definition.** A *category* consists of a collection$^{35}$ of *objects* and, for each pair of objects $A$ and $B$, a collection of *morphisms* $Mor(A, B)$ from $A$ to $B$. There is an operation of composition $\circ : Mor(A, B) \times Mor(B, C) \to Mor(A, C)$ that takes $(f, g)$ to $g \circ f$. This operation must satisfy two axioms:

1. Every object $A$ has an *identity* morphism $id_A \in Mor(A, A)$ such that for all morphisms $f \in Mor(A, B)$, we have $f \circ id_A = id_B \circ f = f$.
2. Composition of morphisms is associative, namely $(f \circ g) \circ h = f \circ (g \circ h)$.

### Examples

- The category **Set** has objects that are sets, and its morphisms are functions between sets.
- The category **Vect**$_k$ has objects that are finite-dimensional vector spaces over a field $k$, and its morphisms are linear maps between vector spaces.
- The category **Group** has objects that are groups, and its morphisms are group homomorphisms between groups.
- The category **Top** has objects that are topological spaces, and its morphisms are continuous functions between spaces.

The above example illustrates that a category often consists of a collection of sets endowed with additional structure, with morphisms the functions on the underlying set that respect this structure. Then the composition law is usually given by the composition of the functions on these underlying sets. However, not all categories arise as collections of objects with additional structure.

It is an easy exercise to see that the identity morphism is unique, as

$$\text{id}_A = \text{id}_A \circ \text{id}'_A = \text{id}'_A$$

**Definition.** A morphism $f \in Mor(A, B)$ is an *isomorphism* if there exists $g \in Mor(B, A)$ such that $f \circ g = id_B$ and $g \circ f = id_A$. In such a case, $g = f^{-1}$ is the inverse of $f$.

It is easy to see that the identity is an isomorphism. Also, if $f$ is an isomorphism, then $f^{-1}$ is an isomorphism. If $f$ and $g$ are isomorphisms, then $f \circ g$ is an isomorphism.

$^{35}$To be precise, a category consists of a *class* of objects, as sometimes there may be too many objects to be a set.

64

<!-- page 65 -->

At this point, you should notice that the properties of the collection of isomorphisms are similar to those of a group. There is an identity element, a composition law, and inverses. However, the collection of isomorphisms of a category differs from a group, as it is not always possible to compose two isomorphisms. If we eliminate the problem, however, we indeed obtain a group.

**Definition.** *The automorphism group of A is the collection*

$$Aut(A) = \{f \in Mor(A, A) : f \text{ is an isomorphism}\}$$

under composition of morphisms.

# Examples

- In Set, the isomorphisms are precisely the bijective functions on sets. Then given a finite set A with n elements, we have Aut(A) ≃ S_n.
- In Vect_k, the isomorphisms are the linear isomorphisms between vector spaces. If V is an n-dimensional vector space R, then Aut(V) ≃ GL(n, R).

Note that in both of these examples, if A and B are isomorphic, then Aut(A) ≃ Aut(B) as groups. However, this isomorphism often depends on a choice of an isomorphism between A and B to identify the two objects. We can then recast the definition of a group in terms of category theory.

**Definition.** *A group is a category with a single object in which all morphisms are isomorphisms.*

One strength of category theory is that it easily allows one to generalize definitions far beyond their original scope.

**Definition.** *A groupoid is a category in which all morphisms are isomorphic.*

Since morphisms may map from/to different objects, the composition of two morphisms is not always defined.

# Examples

- The category that consists of sets as objects and bijections as morphisms is a groupoid.
- The category that consists of topological spaces as objects and homeomorphisms as morphisms is a groupoid.

Both of these examples are not particularly interesting, as they are simply obtained from an existing category by restricting attention to only isomorphisms. We will soon construct a more interesting groupoid from a topological space by letting the objects be points in the space and taking the morphisms to be homotopy classes of paths between two points.

Just like a category often consists of objects with structure-preserving maps between them, there is a notion of a structure-preserving map between categories. In algebraic topology, we will often

65

<!-- page 66 -->

associate a topological space X to an algebraic invariant  \( A(X) \)  such as groups or vector spaces. We would further like this association to behave with the continuous maps on X. Namely, we would like a continuous map  \( X \to Y \)  to induce a morphism  \( A(X) \to A(Y) \) . This associaton of morphisms should satisfy some nice properties, namely that it should respect composition and isomorphisms. This will provide a way to construct algebraic invariants of topological spaces.

Definition. Let C and D be categories. A functor  \( F : C \to D \)  is an assignment of each object  \( X \in C \)  to an object  \( F(X) \in D \)  as well as an assignment of each morphism  \( f \in \text{Mor}_{\mathbb{C}}(X, Y) \)  to a morphism  \( F(f) \in \text{Mor}_{\mathbb{D}}(F(X), F(Y)) \) . This should satisfy

1. \( F(id_X) = id_{F(X)} \), namely \( F \) respects the zero-fold composition of morphisms.
2. \(F(f\circ g) = F(f)\circ F(g)\)

### Examples

- The forgetful functor takes an object of Group, Top, or \(\mathrm{Vect}_k\) to the underlying set and a morphism to the underlying function on sets.
- Given a vector space \( V \in \mathsf{Vect}_k \), there is a functor \( F: \mathsf{Vect}_k \to \mathsf{Vect}_k \) given by \( F(W) = \operatorname{Hom}(V, W) \). A linear map \( f: W \to U \) induces a linear map \( \operatorname{Hom}(V, W) \to \operatorname{Hom}(V, U) \) given by taking \( \varphi \in \operatorname{Hom}(V, W) \) to \( f \circ \varphi \in \operatorname{Hom}(V, U) \).

### Homotopy

One goal of algebraic topology is to study spaces up to continuous deformation, often parameterized by the interval \( I = [0,1] \). This is homotopy.

Definition. Let \( f, g: X \to Y \) be continuous maps. A homotopy between \( f \) and \( g \) is a continuous map \( F: X \times [0,1] \to Y \) such that \( F(x,0) = f(x) \) and \( F(x,1) = g(x) \) for all \( x \in X \). In such a case, \( f \) and \( g \) are homotopic and we write \( f \simeq g \).

It is often convenient to view the parameter in \( I \) as describing a deformation of the map \( f \) to \( g \) over time.

Definition. If f is homotopic to a constant map, then f is nullhomotopic.

If Y is path-connected, any two nullhomotopic paths are homotopic. \( ^{36} \)

Definition. A path in a space \( X \) from \( x_0 \) to \( x_1 \) is a continuous map \( f: I \to X \) such that \( f(0) = x_0 \) and \( f(1) = x_1 \).

In turns out the studying general paths in a space is not too interesting, as any map from a contractible space is always nullhomotopic. If we fix endpoints, however, the picture becomes much more interesting.

\( ^{36} \) Take one path along a homotopy to a point, move the point along a path to the other point, and the apply the homotopy for the other map in reverse.

66

<!-- page 67 -->

**Definition.** A **homotopy of paths** is a homotopy between $f, g: I \to X$ where $f(0) = g(0) = x_0$ and $f(1) = g(1) = x_1$ that fixes the endpoints at all time. More explicitly, there exists a homotopy $F: I \times I \to X$ such that $F(s, 0) = f(s)$, $F(s, 1) = g(s)$, $F(0, t) = x_0$, $F(1, t) = x_1$. In such a case, we write $f \simeq_p g$.

![img-10.jpeg](img-10.jpeg)

**Lemma.** Homotopy $\simeq$ and path homotopy $\simeq_p$ are equivalence relations.

*Proof.* A map $f$ is homotopic to itself by taking the constant homotopy $F(x, t) = f(x)$.

If $f \simeq g$ under a homotopy $F(x, t)$, then $g \simeq f$ via reversing the homotopy $G(x, t) = F(x, 1 - t)$.

If $f \simeq g$ under the homotopy $F$ and $g \simeq h$ under the homotopy $G$. We compose these two homotopies, reparameterizing each appropriately.

$$H(x, t) = \begin{cases} F(x, 2t) & t \in [0, 1/2] \\ G(x, 2t - 1) & t \in [1/2, 1] \end{cases}$$

$H$ is continuous because $F$ and $G$ are and they agree on the intersection of their domains.

None of the proof involved adjusting endpoints, so this also shows $\simeq_p$ is an equivalence relation as well.

![img-11.jpeg](img-11.jpeg)

We denote the (path) homotopy equivalence class of $f$ by $[f]$.

67

<!-- page 68 -->

### The straight line homotopy

**Lemma.** Let $f, g$ be any paths in $\mathbb{R}^n$ from $x_0$ to $x_1$. Then $f \simeq_p g$.

*Proof.* Define the straight line homotopy between $f$ and $g$ by

$$F(s, t) = (1 - t)f(s) + tg(s)$$

This is a parameterization of the line segment between $f(s)$ and $g(s)$.

**Remark.** This result holds more generally in any convex subset of $\mathbb{R}^n$, as the line segment between any two points in a convex subset is contained in the subset.

This also holds for any maps, not just paths, into $\mathbb{R}^n$. This means that $\mathbb{R}^n$, and convex sets more generally, are homotopically trivial.$^a$

$^a$There are many other homotopically trivial/contractible spaces, but one must be more clever about interpolation.

### Example

- In $\mathbb{R}^2 \setminus \{0\}$, the two paths from $(-1, 0)$ to $(1, 0)$ that pass above and below the missing origin are not homotopic. We don't yet have the tools to prove that formally, however.

This idea will provide a proof that $\mathbb{R}^2 \setminus \{0\}$ is not homeomorphic to $\mathbb{R}^2$, and also that $\mathbb{R}^2$ is not homeomorphic to $\mathbb{R}$.

Homotopy classes of paths in a given space $X$ form a category, and this category is a groupoid. The key operation will be the composition/concatenation of paths.

**Definition.** Given a path $f$ from $x$ to $y$ and a path $g$ from $y$ to $z$, we define the path $f * g$ from $x$ to $z$ by

$$(f * g)(t) = \begin{cases} f(2t) & t \in [0, 1/2] \\ g(2t - 1) & t \in [1/2, 1] \end{cases}$$

Note that path homotopy is not associative, but only associative up to path homotopy due to path parameterization details. One could equally well parameterize by all intervals, but this also ultimately has its own disadvantages.

**Lemma.** Path concatenation is well-defined on homotopy classes of paths. Namely, provided that $f(1) = g(0)$ and $f \simeq_p f'$ and $g \simeq_p g'$ then $f * g \simeq_p f' * g'$.

*Proof.* We define the homotopy

$$(F * G)(s, t) = \begin{cases} F(2s, t) & s \in [0, 1/2] \\ G(2s - 1, t) & s \in [1/2, 1] \end{cases}$$

68

<!-- page 69 -->

![img-12.jpeg](img-12.jpeg)

Then we define * on homotopy classes of paths by [f]*[g] = [f*g]. The main claim will be that this operation * is associative, has an identity, as has inverses. Thus path homotopy classes in X form a groupoid with objects points of X and morphisms the homotopy classes of paths between two points.

This operation is not always interesting, though. The space Z is totally disconnected, so there are only morphisms on each point in the space.

Given a point x ∈ X, the identity of x in this groupoid will be the homotopy class [e_x], where e_x : I → X is the constant path e_x(s) = x.

Given a path f : I → X, the homotopy inverse of f is the path f̄ : I → X given by running f backwards for f̄(s) = f(1 - s). We will show that this is indeed a homotopy inverse next lecture and show that * is associative.

We then fix all paths at one point to obtain a group associated to the topological space X.

69

<!-- page 70 -->

# 10/28/2019 - The Fundamental Group(oid)

Today we will dive deeper into algebraic topology. Recall that we were looking at paths in a space X, which are continuous maps I → X. We defined the following notion of ‘sameness’ for paths.

Definition. A path-homotopy between paths f, g : I → X from x to y is a continuous map F : I × I → X such that F(s, 0) = f(s), F(s, 1) = g(s), F(0, t) = x, F(1, t) = y.

In general, we will restrict out attention to individual path-components and take it for granted that we can understand these individual pieces of a space by probing them with maps from the interval.

We defined a concatenation operation on paths f, g : I → X by declaring f * g to be the path obtained by first running f and then running g. In formulas, this is

$$(f * g)(s) = \begin{cases} f(2s) & s \in [0, 1/2] \\ g(2s - 1) & s \in [1/2, 1] \end{cases}$$

We proved last lecture that this is well-defined on paths up to homotopy equivalence, and thus defines an operation on equivalence classes [f] * [g]. When we pass to path homotopy, we obtain the following desirable property.

Lemma. * on homotopy classes of paths is associative, has an identity, and has inverses. Then the collection of all homotopy classes of paths along with * is the fundamental groupoid of X, where the objects of this groupoid are the points of X and the morphisms from x to y are the homotopy classes of maps from x to y.

Proof. The identity morphism at a point x ∈ X will be given by id_x = [e_x], where e_x is the constant path e_x(s) = x. We need to check that the identity behaves as expected under composition.

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

The homotopy

$$F(s, t) = \begin{cases} f\left(\frac{s}{1 - t/2}\right) & s \in [0, 1 - t/2] \\ y & s \in [1 - t/2, 1] \end{cases}$$

is a path homotopy from f to f * e_y. A similar computation shows that id_x ∘ [f] = [f] as well.

Given a path f, define f̄(s) = f(1 - s). f̄ runs the path f backwards. The claim is that [f] * [f̄] = id_x

70

<!-- page 71 -->

and $[\overline{f}] * [f] = \mathrm{id}_y$. The diagram

![img-15.jpeg](img-15.jpeg)

suggests that we should consider a family of paths that travel partially along $f$ and then return. Explicitly, the homotopy

$$F(s, t) = \begin{cases} f(2ts) & s \in [0, 1/2] \\ f(2t(1 - s)) & s \in [1/2, 1] \end{cases}$$

is a path homotopy from $e_x$ to $f * \overline{f}$.

Finally, we check associativity. The reason $(f * g) * h \neq f * (g * h)$ literally is that, in the first expression, we spend $1/4$ of the time on $f$ and $g$ and $1/2$ of the time on $h$, whereas in the second expression we spend $1/2$ of the time on $f$ and $1/4$ of the time on $g$ and $h$. Then the diagram

![img-16.jpeg](img-16.jpeg)

shows we can rescale the time parameter as desired.

Although groupoids capture much information about a space, they can be difficult to deal with. For that reason, we will restrict our attention to a single point to obtain a group. We choose a **base point** $x_0 \in X$ and consider only **loops** at $x_0$, namely paths that begin and end at $x_0$.

**Definition.** The set of path homotopy classes of loops based at $x_0$, with operation $*$, is the **fundamental group** of $X$ at $x_0$, denoted $\pi_1(X, x_0)$.37

37The notation is suggestive, as there are higher homotopy groups defined as homotopy classes of maps from higher-dimensional spheres into $X$.

71

<!-- page 72 -->

The fundamental group is of great importance in topology. The fact that it is a group follows immediately from the previous lemma, as  \( \pi_{1}(X) \)  is given as the automorphism group of a point  \( x_{0} \in X \) . We will see that this group is often nontrivial and examine its behavior under maps. \( ^{38} \)  Today we will introduce some basic notions.

#### Example

- In \(\mathbb{R}^n\), or a convex subspace of \(\mathbb{R}^n\), every loop at \(x_0\) is homotopic to the constant loop via the straight line homotopy. Explicitly, the path homotopy

\[
F (t, s) = (1 - t) f (s) + t x _ {0}
\]

does the trick. Therefore \(\pi_1(\mathbb{R}^n,x_0) = \{\mathrm{id}\} = 1\)

Definition. A space \( X \) is simply connected if \( X \) is nonempty, path-connected, and for some \( x_0 \) we have \( \pi(X, x_0) = 1 \).

Then the above example should then be interpreted as saying that  \( R^{n} \) , and any convex subset of  \( R^{n} \) , is simply-connected.  \( S^{n} \)  is simply-connected when  \( n \geq 2 \) . However,  \( S^{1} \)  is not simply-connected, and we will study  \( \pi_{1}(S^{1}, x_{0}) \)  in great detail.

It turns out that, when restricting to the same path component, \(\pi_1(X,x_0)\) is independent of the base point \(x_0\).

Proposition. Let  \( x_{0} \)  and  \( x_{1} \)  be points in a path-connected space X. Then  \( \pi_{1}(X,x_{0})\simeq\pi_{1}(X,x_{1}) \) .

Proof. We must determine how to relate loops at  \( x_{0} \)  to those at  \( x_{1} \) .

![img-17.jpeg](img-17.jpeg)

For a loop \( f \) at \( x_0 \) and a path \( \alpha \) from \( x_0 \) to \( x_1 \), we obtain a loop at \( x_1 \) by the concatenation \( \overline{\alpha} * f * \alpha \). This yields a map

\[
\widehat {\alpha}: \pi_ {1} (X, x _ {0}) \to \pi_ {1} (X, x _ {1})
\]

\[
[ f ] \mapsto [ \overline {{\alpha}} * f * \alpha ] = [ \alpha ] ^ {- 1} * [ f ] * [ \alpha ]
\]

\( ^{38} \) This will require the technology of covering spaces, which are a way of unrolling a topological space in a discrete way.

72

<!-- page 73 -->

We will show that $\widehat{\alpha}$ is a group isomorphism, namely that it is a homomorphism with an inverse. If $a, b \in \pi_1(X, x_0)$ then we have

$$\begin{array}{l} \widehat{\alpha}(a * b) = [\alpha]^{-1} * a * b * [\alpha] \\ = [\alpha]^{-1} * a * [\alpha] * [\alpha]^{-1} * b * [\alpha] \\ = \widehat{\alpha}(a) * \widehat{\alpha}(b) \end{array}$$

by associativity and identity. Let $\beta = \overline{\alpha}$ be the path $\alpha$ run in reverse. The claim is that $\widehat{\beta}$ is an inverse to $\widehat{\alpha}$. Indeed, for $a \in \pi_1(X, x_0)$ we have

$$\begin{array}{l} \widehat{\beta} \circ \widehat{\alpha}(a) = \widehat{\beta}([\alpha]^{-1} * a * [\alpha]) \\ = [\beta]^{-1} * [\alpha]^{-1} * a * [\alpha] * [\beta] \\ = a \end{array}$$

Therefore $\widehat{\beta} \circ \widehat{\alpha} = \text{id}$, and the same argument proves $\widehat{\alpha} \circ \widehat{\beta} = \text{id}$. Therefore $\pi_1(X, x_0) \simeq \pi_1(X, x_1)$. $\square$

This result can be stated categorically as well. If $x_0, x_1$ are isomorphic in the fundamental groupoid, namely there exists a path from $x_0$ to $x_1$, then $\text{Aut}(x_0) \simeq \text{Aut}(x_1)$. This proposition should not be too surprising, as it says that studying continuous loops at a point does not depend on continuous moving the base point around the space.

**Corollary.** If $X$ is path-connected, then up to isomorphism $\pi_1(X, x_0)$ is independent of the base point $x_0$.

**Corollary.** A loop $f$ at $x_0$ induces an automorphism $\widehat{f}: \pi_1(X, x_0) \to \pi_1(X, x_0)$. This yields a group action of $\pi_1(X, x_0)$ on itself via conjugation:

$$a \mapsto [f]^{-1} * a * [f]$$

Such a map is an **inner automorphism** of $\pi_1(X, x_0)$.

An obvious next question would be the extend to which the fundamental group is a natural construction on a space. In other words, how does changing the space $X$ affect the fundamental group?

The key idea will be that $\pi_1$ can be understood as a functor from the category of *pointed topological spaces* to the category of groups.

**Definition.** The **category of pointed topological spaces** is the category $\text{Top}_*$, whose objects consist of pairs $(X, x_0)$, where $X$ is a space and $x_0 \in X$ a point. The morphisms of $\text{Top}_*$ are continuous maps that respect the points, namely a map $f: X \to Y$ such that $f(x_0) = y_0$.

**Proposition.** A morphism $h: (X, x_0) \to (Y, y_0)$ induces a group homomorphism $h_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$ defined by

$$h_*([f]) = [h \circ f]$$

We must check that this homomorphism is well-defined, namely that if $[f] = [f']$ then $[h \circ f] = [h \circ f']$. This is simple, though, as if $F: I \times I \to X$ is a homotopy between $f$ and $f'$ then $h \circ F$ is a homotopy between $h \circ f$ and $h \circ f'$. It is also easy to see that $h \circ (f * g) = (h \circ f) * (h \circ g)$, so together these facts imply we have a well-defined homomorphism

$$h_*([f] * [g]) = h_*([f]) * h_*([g])$$

73

<!-- page 74 -->

**Corollary.** $\pi_1: \text{Top}_* \to \text{Group}$ is a functor. It sends an object $(X, x_0) \in \text{Top}_*$ to $\pi_1(X, x_0)$ and a morphism $h: (X, x_0) \to (Y, y_0)$ to the induced map $h_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$.

Note that it still remains to check that $\pi_1$ respects composition of morphisms, namely that if $h: (X, x_0) \to (Y, y_0)$ and $k: (Y, y_0) \to (Z, z_0)$ are morphisms then $(k \circ h)_* = k_* \circ h_*$.

$$\pi_1(X, x_0) \xrightarrow{h_*} \pi_1(Y, y_0) \xrightarrow{k_*} \pi_1(Z, z_0)$$

But this follows immediately from the associativity of function composition, as

$$\begin{aligned} (k \circ h)_*([f]) &= [(k \circ h) \circ f] \\ &= [k \circ (h \circ f)] \\ &= k_*([h \circ f]) \\ &= k_* \circ h_*([f]) \end{aligned}$$

Since functors map isomorphisms to isomorphisms (as inverses are sent to inverses), we obtain the following result for free.

**Corollary.** If $h: (X, x_0) \to (Y, y_0)$ is a homeomorphism, then $h_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$ is an isomorphism.

This is good, because we would like to view homeomorphic spaces as the same, so they should have the same fundamental group. Homeomorphism is a very strong idea of sameness for topological spaces, however, and we will see later than $\pi_1$ is invariant under a much weaker notion, *homotopy equivalence*.

74

<!-- page 75 -->

# 10/30/2019 - Covering Spaces, Path Lifting

Given a pointed topological space  \( (X,x_{0}) \) , we associate to it the fundamental group  \( \pi_{1}(X,x_{0}) \) . This group consists of homotopy classes of loops based at  \( x_{0} \) , with product given by concatenating two loops. Up to isomorphism,  \( \pi_{1}(X,x_{0}) \)  is independent of basepoint, and a continuous map  \( (X,x_{0})\to(Y,y_{0}) \)  induces a homomorphism  \( \pi_{1}(X,x_{0})\to\pi_{1}(Y,y_{0}) \) .

To compute \(\pi_1(X, x_0)\), we will introduce covering spaces. These are topological spaces that 'sit above' \(X\) in some discrete way.

Definition. Let \( p: E \to B \) be a continuous, surjective map. \( p \) evenly covers an open set \( U \subset B \) if

\[
p ^ {- 1} (U) = \bigsqcup_ {\alpha \in A} V _ {\alpha}
\]

where  \( V_{\alpha} \subset E \)  are disjoint open subsets and  \( p|_{V_{\alpha}} : V_{\alpha} \to U \)  is a homeomorphism.

![img-18.jpeg](img-18.jpeg)

Equivalently, we can say that there is a homeomorphism \( p^{-1}(U) \to U \times A \), where \( A \) has the discrete topology, such that

![img-19.jpeg](img-19.jpeg)

commutes.

Definition. If  \( p: E \to B \)  is continuous and surjective such that every point  \( b \in B \)  has a neighborhood evenly covered by p, then E is a covering space of B with covering map p.

The equivalent definition above means that we can alternatively characterize covering spaces as fiber bundles with discrete fiber.

75

<!-- page 76 -->

### Examples

- Let $X$ be any topological space and $A$ be discrete. Then $p: X \times A \to X$ is a covering map. This is the trivial $|A|$-fold cover of $X$, and the entire space $X$ is evenly covered by $p$.
- Define $p: \mathbb{R} \to S^1$ by $p(t) = (\cos t, \sin t)$.

![img-20.jpeg](img-20.jpeg)

To show an arbitrary point has a neighborhood that is evenly covered, consider the point $(1, 0)$. Let $U = \{(x, y) \in S^1 : x > 0\}$. $U \subset S^1$ is open in the subspace topology. Then we have

$$p^{-1}(U) = \bigsqcup_{n \in \mathbb{Z}} (2\pi n - \pi/2, 2\pi n + \pi/2)$$

$p$ restricted to each $(2\pi n - \pi/2, 2\pi n + \pi/2)$ is a homeomorphism onto $U$.

In other words, above each point a covering space is a collection of sheets, but these may be connected together nontrivially globally. These covering spaces are intimately related to homotopy, as they allow us to unroll paths of $X$ in interesting ways.

**Proposition.** Let $p: E \to B$ and $q: E' \to B'$ be covering maps. Then $(p \times q): E \times E' \to B \times B'$ is a covering map.

### Example

- The map $p \times p: \mathbb{R}^2 \to S^1 \times S^1$, where $p: \mathbb{R} \to S^1$ is the above covering map of the circle, is a cover of the torus.

![img-21.jpeg](img-21.jpeg)

Proof. Given $(b, b') \in B \times B'$, there exists open $U \subset B, U' \subset U'$ containing $b, b'$ that are evenly

76

<!-- page 77 -->

covered by $p, p'$, respectively. The claim is that $U \times U'$ is evenly covered by $p \times p'$. For if

$$p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha \subset E$$

$$p'^{-1}(U') = \bigsqcup_{\beta \in B} V'_\beta \subset E'$$

then

$$(p \times p')^{-1}(U \times U') = p^{-1}(U) \times p^{-1}(U') = \bigsqcup_{(\alpha, \beta) \in A \times B} V_\alpha \times V_\beta \subset E \times E'$$

**Proposition.** If $p : E \to B$ is a covering map and $B_0 \subset B$ a subset, then $E_0 = p^{-1}(B_0)$ is a covering space of $B_0$ with covering map $p|_{E_0}$.

For example, restricting one's attention to the meridian and the longitude of the torus $S^1 \times S^1$ yields a covering space of $S^1 \vee S^1$ (the figure-eight space) that is the infinite grid, where the horizontal and vertical lines are $2\pi$ apart.

The following important fact is an exercise on the homework assignment.

**Proposition.** Suppose $B$ is connected and $p : E \to B$ is a covering map. Then for all $x, y \in B$, the fibers $p^{-1}(x)$ and $p^{-1}(y)$ have the same cardinality.

**Definition.** Let $B$ be connected and $p : E \to B$ be a covering map. If $p^{-1}(x)$ is finite, then $d = f^{-1}(x)$ is the **degree** of $p$.

### Example

- The covering map $p : \mathbb{R} \to S^1$ has infinite degree.
- View $S^1 \subset \mathbb{C}$ as the complex numbers of norm 1. Then the map

$$p : S^1 \to S^1$$

$$e^{i\theta} \mapsto e^{ni\theta}$$

can be seen to have degree $n$.

### Lifting

It will be extremely useful to develop criteria for when it is possible to lift a map $f : Y \to X$ to another map $\widetilde{f} : Y \to E$ such that

$$Y \xrightarrow[\widetilde{f}]{\widetilde{f}} B$$

commutes. This lifting will eventually allow us to determine homotopy classes of maps into $X$.

77

<!-- page 78 -->

The first observation is that if \( p: E \to B \) is a covering map, then there exists a local lift of any map \( f: X \to B \). Namely, if \( f(X) \subset U \), where \( U \) is evenly covered, then if \( V_{\alpha} \) is a sheet over \( U \) we can define \( \widetilde{f} = (p|_{V_{\alpha}})^{-1} \circ f \). We will next show that it is always possible to lift paths, and homotopies of paths, even if they leave a single evenly covered subspace of \( B \).

### Example

- Consider the usual covering map \( p: \mathbb{R} \to S^1 \) given by \( p(x) = (\cos x, \sin x) \). Let \( f: I \to S^1 \) be the path \( f(s) = (\cos \pi s, \sin \pi s) \). This path has infinitely many lifts to \( \mathbb{R} \), specified by choosing an initial point.

Theorem. Let \( p: E \to B \) be a covering map and \( f: [0,1] \to B \) a path with \( f(0) = b \). Given \( e \in p^{-1}(b) \), there exists a unique lift \( \widetilde{f}: [0,1] \to E \) such that \( \widetilde{f}(0) = e \) and \( p \circ \widetilde{f} = f \).

The key idea of the proof is that, as long as the path remains in an evenly covered subspace, there is a unique choice of the a lift for the path.

Proof. Cover \( B \) by open subsets \( U_{\alpha} \) that are themselves evenly covered by \( p \). Then the inverse images \( f^{-1}(U_{\alpha}) \) cover the interval [0, 1]. By the Lebesgue number lemma, there exists \( \delta > 0 \) such that \( (s, s + \delta) \) lies in a single set \( f^{-1}(U_{\alpha}) \), and equivalently \( f(s, s + \delta) \) lies in a single \( U_{\alpha} \). Thus we can subdivide the path \( 0 = s_0 \leq s_1 \leq \ldots \leq s_n = 1 \) such that \( f(s_i, s_{i+1}) \subset U_{\alpha} \) for some \( \alpha \) depending on \( i \).

Define \(\widetilde{f}(0) = e\). Assume that \(\widetilde{f}\) is defined on \([0, s_i]\). By construction, \(f(s_i, s_{i+1})\) lies in a single evenly covered \(U\). \(f(s_i)\) is defined, so let \(V \subset p^{-1}(U)\) be the slice above \(U\) containing this \(f(s_i)\). For \(s \in [s_i, s_{i+1}]\), define \(f(s) = (p|_V)^{-1} \circ f(s)\). This agrees with the definition of \(f|_{[0, s_i]}\), and it is continuous on \([s_i, s_{i+1}]\) since it is the composition of continuous maps.

This choice of \(\widetilde{f}\) is unique, as at each step the definition of \(\widetilde{f}\) on \([s_i, s_{i+1}]\) is forced.

The next theorem says that we can also lift homotopies.

Theorem. Let \( p: E \to B \) be a covering map and \( F: I \times I \to B \) a homotopy with \( F(0,0) = b \). Given \( e \in p^{-1}(b) \), there exists a unique lift \( \widetilde{F}: I \times I \to E \) such that \( \widetilde{F}(0,0) = e \) and \( p \circ \widetilde{F} = F \).

The proof is analogous to the previous one, where we now use the Lebesgue number lemma to conclude that there is a small enough subdivision of  \( I \times I \)  such that the image of each subrectangle lies in an evenly covered subset of B. \( ^{39} \)

Remark. If \( F \) is a path homotopy from \( f \) to \( g \) in \( B \), then \( \widetilde{F} \) is a path homotopy from \( \widetilde{f} \) to \( \widetilde{g} \) in \( E \). In particular, if \( f \) and \( g \) are path homotopic then the lifts \( \widetilde{f} \) and \( \widetilde{g} \) beginning at \( e \) also end at the same point \( e' = \widetilde{f}(1) = \widetilde{g}(1) \).

This is an important observation that relates homotopy to path lifting.

\( ^{39} \) In general, any map from a simply connected space can be lifted to a covering space. We will give a more complete characterization of lifting and covering spaces later.

78

<!-- page 79 -->

Loops don't always lift to loops, however, For example, lifting the loop that goes around the circle $S^1$ yields a path in $\mathbb{R}$. This will be precisely how we show that such a loop on $S^1$ is not homotopic to a constant loop.

Given a starting point $e_0 \in p^{-1}(b_0)$, the endpoint of the lift of a loop at $b_0$ is uniquely determined. Furthermore, path homotopic loops has lifts with the same endpoint. This means there is a well-defined lifting correspondence $\varphi : \pi_1(B, b_0) \to p^{-1}(b_0)$ that sends a homotopy class $[f]$ to $\varphi([f]) = \widetilde{f}(1)$.

# The fundamental group of the circle is nontrivial

- Let $p : \mathbb{R} \to S^1$ be the usual covering map and $b_0 = (1, 0)$. If $f$ loops around the circle $k$ times, then $\widetilde{f}(1) = 2\pi k$. Thus $\varphi([f]) = 2\pi k$. We have a map $\varphi : \pi_1(S^1, b_0) \to 2\pi \mathbb{Z}$ that is a surjection. Therefore $\pi_1(S^1, b_0)$ is at least as large as $\mathbb{Z}$ as a set. We will show that this is in fact a group homomorphism.

Next time we will show additional properties of the lifting correspondence, namely why it is often surjective and sometimes injective. We will consider more examples of spaces in algebraic topology generated via quotients and gluing.

79

<!-- page 80 -->

# 11/4/2019 - Fundamental Group of the Circle, Quotients and Gluing

Recall that given a covering map $p : E \to B$, any path $f : I \to B$ beginning at $f(0) = b$ can be lifted uniquely to a path $\widetilde{f} : I \to E$ beginning at $e \in p^{-1}(b)$. We also saw that homotopies lift, which means homotopic paths have homotopic lifts, and in particular the lifts end at the same point.

This implies there is a lifting correspondence $\varphi : \pi_1(B, b_0) \to p^{-1}(b_0)$ defined by $\varphi([f]) = \widetilde{f}(1)$ well-defined on homotopy classes of loops.

# Example

- Consider the usual covering map

$$\begin{array}{l} p : \mathbb{R} \to S^1 \\ x \mapsto (\cos 2\pi x, \sin 2\pi x) \end{array}$$

The loop $f$ that goes once clockwise around the circle lifts to a path in $\mathbb{R}$ from 0 to 1. Thus $\varphi([f]) = 1$. In general, $\varphi$ takes the loop that travels $k$ times around the circle to $k \in \mathbb{Z}$.

Lemma. If $E$ is path-connected, then the lifting correspondence $\varphi$ is surjective.

Proof. Let $f : I \to E$ be a path from $e_0 \in p^{-1}(b_0)$ to any $e \in p^{-1}(b_0)$. Then the projection $g = p \circ f$ is a loop in $B$ based at $b_0$. $f$ is a lift of this loop $g$, which implies $\varphi([g]) = e$. $\square$

Usually, the lifting correspondence need not be injective. However, given certain conditions on the covering space $E$ we can guarantee that this correspondence is a bijection.

Proposition. If $p : E \to B$ is a covering map and $E$ is simply connected,⁴⁰, then the lifting correspondence $\varphi$ is a bijection.

Proof. $\varphi$ is surjective by the previous lemma. To show $\varphi$ is injective, suppose $\varphi([f]) = \varphi([g])$. Then the lifts $\widetilde{f}$ and $\widetilde{g}$ has the same endpoint $e$.

The claim is that $\widetilde{f}$ and $\widetilde{g}$ are path-homotopic. $\widetilde{f} * \widetilde{g}^{-1}$ is a loop based at $e_0$, homotopic to the constant loop. Then

$$\widetilde{f} \simeq \widetilde{f} * e \simeq \widetilde{f} * \widetilde{g}^{-1} * \widetilde{g} \simeq e * \widetilde{g} \simeq \widetilde{g}$$

where we are using that $\widetilde{g}^{-1} * \widetilde{g} \simeq e$ and $\widetilde{f} * \widetilde{g}^{-1} \simeq e_0$. Let $\widetilde{F}$ be a homotopy between $\widetilde{f}$ and $\widetilde{g}$. Then $F = p \circ \widetilde{F}$ is a path homotopy between $f$ and $g$, which implies $[f] = [g]$. So $\varphi$ is injective, as desired. $\square$

Theorem. We have $\pi_1(S^1) \simeq \mathbb{Z}$ as groups.

⁴⁰This is the universal cover of $B$.

80

<!-- page 81 -->

This tells us the group structure on $\pi_1(S^1)$ (rather than merely the cardinality).

Proof. Consider the lifting correspondence $\varphi : \pi_1(S^1, (1, 0)) \to \mathbb{R}$ on the covering space $\mathbb{R} \to S^1$. $\varphi$ is a bijection by the previous theorem, so it remains to confirm that this map respects composition in $\pi_1(S^1, (1, 0))$.

Let $[f], [g] \in \pi_1(S^1, (1, 0))$ with $\varphi([f]) = n$ and $\varphi([g]) = m$. Then the lifts $\widetilde{f}$ and $\widetilde{g}$ beginning at 0 end at $n$ and $m$, respectively. Define $h : I \to \mathbb{R}$ by $h(s) = n + \widetilde{g}(s)$. This is the lift of $g$ starting at $n$. Since $n = \widetilde{f}(1)$, we know that $\widetilde{f} * h$ is a path in $\mathbb{R}$ that is the lift of $f * g$ beginning at 0 and ending at $n + m$. Therefore $\varphi([f] * [g]) = n + m$.

Remark. The same method yields $\pi_1(S^1 \times S^1) \simeq \mathbb{Z} \times \mathbb{Z}$.

### Gluing and quotients

We will return to some point set topology,⁴¹ as gluing and quotients will be an important source of examples in algebraic topology.

#### Examples

- The quotient of the interval $[0, 1]$ by the equivalence relation $0 \sim 1$ that identifies the endpoints yields the circle $S^1$.
- The quotient of the square $[0, 1]^2$ by the equivalence relation that identifies $(0, t) \simeq (1, t)$ yields the cylinder $[0, 1] \times S^1$. Also gluing along $(s, 0) \simeq (s, 1)$ yields the torus $S^1 \times S^1$.

These constructions are usually best illustrated with a gluing diagram.

The construction that underlies these examples is the quotient topology.

Definition. Let $X$ be a topological space, $A$ a set, and $f : X \to A$ be a surjective map.⁴² The quotient topology on $A$ is defined by declaring $U \subset A$ open if and only if $f^{-1}(U) \subset X$ is open.

This indeed defines a topology on $A$, as unions and intersections behave well with preimages. The quotient topology is alternatively characterized as the finest topology on $A$ such that the quotient map $f : X \to A$ is continuous.

Definition. A map $f : X \to Y$ is a quotient map if $f$ is surjective and $U \subset Y$ is open if and only if $f^{-1}(U) \subset X$ is open.

Remark. If $f : X \to Y$ is surjective, continuous, and open, then $f$ is a quotient map.

Note that there are quotient maps that are not necessarily open. The definition only demands that open sets that are the preimage of sets in $Y$ map to open sets, and it does not constrain the

⁴¹'We are going back in time here and must only be careful not to meet the parents of of the fundamental group.' (D. Auroux)

⁴²We can also frame this as an equivalence relation $\sim$ on $X$ by defining $f : X \to X / \sim = A$. Conversely, if $f : X \to A$ is surjective, we obtain an equivalence relation on $X$ by declaring $x \sim x'$ if they lie in the same fiber.

81

<!-- page 82 -->

behavior of $f$ on the other open sets of $X$ that do not arise as such a preimage.

Homeomorphisms are another trivial example of quotient maps (in which case the equivalence relation $\sim$ only identifies $x \sim x$ and nothing else).

### Example

- We can obtain $S^1$ as $[0, 1]$ with 0 identified with 1. Explicitly, the equivalence relation is $0 \sim 1$ with no other distinct points identified. The equivalence classes of $[0, 1]$ are $\{0, 1\}$ along with $\{x\}$ for all $x \in (0, 1)$.

The quotient map $f : [0, 1] \to S^1$ is given by $f(t) = (\cos 2\pi t, \sin 2\pi t)$. $f$ is a quotient map, but it is not open, as the image of the open set $[0, \epsilon)$ is not open in $S^1$.$^a$

$^a[0, \epsilon)$ is not a subset that arises as the preimage of any set in $S^1$.

We can use quotients to attach topological spaces together.

### Attaching topological spaces

- Let $(X_1, x_1), \ldots, (X_n, x_n)$ be pointed topological spaces, with each $X_i \simeq S^1$. Let $A$ be the quotient space of the disjoint union $\bigsqcup X_i$, where the equivalence relation identifies $x_i \sim x_j$ for all $i, j$ and no other distinct points. Then $A$ is the *wedge of $n$ circles*.

![img-22.jpeg](img-22.jpeg)

If $A = X / \sim$ and $f : X \to Y$ is compatible with the equivalence relation, in that $x \sim x'$ implies $f(x) = f(x')$, then $f$ induces a map $\overline{f} : A \to Y$ defined by $\overline{f}([x]) = f(x)$. Compatibility with the equivalence relation guarantees this is well-defined. In such a case, we say that $f$ *factors* through the quotient.

$$\begin{array}{c} X \xrightarrow{f} Y \\ \downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{A} = X / \sim \end{array}$$

Although this makes sense from a set-theoretic perspective, we would like our maps in topology to be continuous as well. Let $q : X \to X / \sim$ be the quotient map.

**Theorem.** If $f : X \to Y$ is continuous and $x \sim x'$ implies $f(x) = f(x')$, then the induced map $\overline{f} : X / \sim \to Y$ is continuous. Conversely, if $\overline{f}$ is continuous, then the composition $f = \overline{f} \circ q$ is continuous.

82

<!-- page 83 -->

Proof. For $U \subset Y$ open, we have that $f^{-1}(U) = q^{-1}(\overline{f}^{-1}(U)) \subset Y$ is open. By definition of the quotient topology, $\overline{f}^{-1}(U)$ is open, as the inverse image $q^{-1}(f^{-1}(U))$ is open. Therefore $\overline{f}$ is continuous. $\square$

### Example

- On $X = \mathbb{R}^n \setminus \{0\}$, define $x \sim y$ if and only if $x$ and $y$ lie on the same line through 0. In other words, $x \sim y$ if and only if $x = \alpha y$ for some nonzero $\alpha \in \mathbb{R}$. It is not difficult to see that this is an equivalence relation.

The quotient space $X / \sim = \mathbb{R}\mathbb{P}^{n-1}$ is real projective space of dimension $n-1$.$^a$ A continuous map $\overline{f}: \mathbb{R}\mathbb{P}^{n-1} \to Y$ is the same as a continuous map $f: \mathbb{R}^n \setminus \{0\} \to Y$ such that $f(\alpha x) = f(x)$ for all $\alpha \in \mathbb{R} \setminus \{0\}$.

- Let $X = [0, 1] \times [0, 1]$. Let

$$A = \{0\} \times [0, 1] = \{(0, y) : y \in [0, 1]\}$$

$$A' = \{1\} \times [0, 1] = \{(1, y) : y \in [0, 1]\}$$

$$B = [0, 1] \times \{0\} = \{(x, 0) : x \in [0, 1]\}$$

$$B' = [0, 1] \times \{1\} = \{(x, 1) : x \in [0, 1]\}$$

- Glue $A$ to $A'$ by the equivalence relation $(0, t) \sim (1, t)$ to obtain the cylinder $S^1 \times [0, 1]$.

![img-23.jpeg](img-23.jpeg)

- We can also glue $A$ to $A'$ by the equivalence relation $(0, t) \sim (1, 1 - t)$. This yields the Möbius strip.

![img-24.jpeg](img-24.jpeg)

- Glue $A$ to $A'$ by $(0, t) \sim (1, t)$ and $B$ to $B'$ by $(s, 0) \sim (s, 1)$ to obtain the torus.

![img-25.jpeg](img-25.jpeg)

- Glue $A$ to $A'$ by $(0, t) \sim (1, t)$ and $B$ to $B'$ by $(s, 0) \sim (1 - s, 1)$ to obtain the Klein

83

<!-- page 84 -->

bottle.

![img-26.jpeg](img-26.jpeg)

- Glue \(A\) to \(A'\) by \((0,t)\sim (1,1 - t)\) and \(B\) to \(B'\) by \((s,0)\sim (1 - s,1)\) to obtain the real projective plane \(\mathbb{RP}^2\).

![img-27.jpeg](img-27.jpeg)

\( ^{a} \) There is an important connection between the sphere and real projective space. One can construct the sphere as a quotient of  \( R^{n} \setminus \{0\} \)  by the same equivalence relation, except restricting scalar multiplication to positive real numbers.

84

<!-- page 85 -->

# 11/6/2019 - The Brouwer Fixed Point Theorem

Today we will discuss two applications of the result $\pi_1(S^1) = \mathbb{Z}$. Both of these are, in some sense, 2-dimensional generalizations of the intermediate value theorem. For example, consider the following two results.

**Theorem.** *Every continuous map $f : I \to I$ has a fixed point, namely there exists $x \in I$ such that $f(x) = x$.*

This follows from the intermediate value theorem applied to the function $g(x) = f(x) - x$. This generalizes to the **Brouwer fixed point theorem**.

**Theorem.** *Every continuous map $f : S^1 \to \mathbb{R}$ has a point $x \in S^1$ such that $f(x) = f(-x)$.*

This follows from the intermediate value theorem applied to the function $g(x) = f(x) - f(-x)$. This generalizes to the **Borsuk-Ulam theorem**.

# Brouwer fixed point theorem

Let $B^n$ be the closed ball of radius 1 in $\mathbb{R}^n$. Then $\partial B^n = S^{n-1}$. The *Brouwer fixed point theorem* is the following result.

**Theorem.** *Let $f : B^n \to B^n$ be a continuous map. Then $f$ has a fixed point, namely there exists $x \in B^n$ with $f(x) = x$.*

This general result requires techniques of *higher homotopy* or *homology*. We will be able to prove the result in dimension 2.

**Theorem.** *Let $f : B^2 \to B^2$ be a continuous map. Then $f$ has a fixed point, namely there exists $x \in B^2$ with $f(x) = x$.*

Recall the notion of a *retraction*.

**Definition.** *Let $A \subset X$ be a subset. A continuous map $r : X \to A$ is a **retraction** if $r|_A : A \to A$ is the identity.*

The theorem that provides the bridge to the Brouwer fixed point theorem is the following result.

**Theorem.** *There does not exist a retraction $r : B^2 \to S^1$.*

In general, a retraction induces a surjective map on fundamental groups, but we can present a more concrete proof as well.

*Proof.* Let $r : B^2 \to S^1$ be a retraction. If $f$ is a loop in $S^1$, then $f$ is a loop in $B^2$. $B^2 \subset \mathbb{R}^2$ is convex, so $f$ is homotopy equivalent to a constant loop. Let $F : I \times I \to B^2$ be such a homotopy. Then the composition $r \circ F : I \times I \to S^1$ is a homotopy from $f$ to the constant loop. This is impossible whenever $[f]$ is nontrivial in $\pi_1(S^1) = \mathbb{Z}$. $\square$

85

<!-- page 86 -->

The higher dimensional analogue of this intermediate theorem is the nonexistence of a retraction $B^n \to S^{n-1}$. We can use this to prove the fixed point theorem.

Proof. Suppose for contradiction there exists $f : B^2 \to B^2$ with $f(x) \neq x$ for all $x \in B^2$. Then define $F : B^2 \to S^1$ by letting $F(x)$ be the intersection of the line through $f(x)$ and $x$ and $S^1$.

![img-28.jpeg](img-28.jpeg)

More explicitly, we have that

$$F(x) = x + t(x - f(x))$$

where $t$ is the positive root of the quadratic equation

$$1 = \|x + t(x - f(x))\|^2$$

which depends on $x$ continuously by the quadratic formula. Thus we have a retraction $F : B^2 \to S^1$, which is a contradiction.

Given the intermediary theorem, the same argument implies that any map $B^n \to B^n$ has a fixed point.

We will develop a bit more theory that will help us understand why this argument worked. The following is a characterization of topologically trivial maps $S^1 \to X$.

**Theorem.** Let $h : S^1 \to X$ be continuous. The following are equivalent.

1. $h$ is nullhomotopic, namely $h$ is homotopic to a constant map.
2. $h$ extends to a continuous map $\overline{k} : B^2 \to X$ such that $k|_{S^1} = h$.
3. The induced $h_* : \pi_1(S^1) \to \pi_1(X)$ is trivial.

Proof. Let $H : S^1 \times I \to X$ be a homotopy between $h$ and a constant map. $\pi : S^1 \times I \to B^2$ given by $\pi(x, t) = (1 - t)x$ is a quotient map and yields a homeomorphism $(S^1 \times I/(x, 1) \sim (x', 1)) \simeq B^2$. $H|_{S^1 \times \{1\}}$ is constant, and thus $H$ factors though the quotient $\overline{H} : B^2 \to X$ with $H|_{S^1 \times \{0\}} = h$. Then $k = \overline{H}$ is the desired extension.

86

<!-- page 87 -->

Let \( h: k|_{S^1} \to X \) be a map, where \( k: B^2 \to X \). We can write \( h = k \circ i \) and use the functoriality of \( \pi_1 \) for

![img-29.jpeg](img-29.jpeg)

which implies \( h_* \) is trivial.

Finally, assume the induced \( h_*: \pi_1(S^1, b_0) \to \pi_1(X, x_0) \) is trivial. Let \( f: I \to S^1 \) be the loop \( f(s) = (\cos 2\pi s, \sin 2\pi s) \), whose homotopy class generates \( \pi_1(S^1) \). \( f \) is also a quotient map and yields and homeomorphism \( ([0, 1]/0 \sim 1) \simeq S^1 \). Define \( g = h \circ f: I \to X \). \( g \) is a loop in \( (X, x_0) \) representing the image \( h_*(f) \). There exists a path homotopy \( G: I \times I \to X \) from \( g \) to the constant path at \( x_0 \). There is a quotient map \( F: I \times I \to S^1 \times I \) given by \( F(s, t) = (f(s), t) \), and it identifies \( (0, t) \sim (1, t) \). \( G \) respects this relation and descends to a map \( \overline{G}: S^1 \times I \to X \). This is the desired homotopy.

Corollary. The identity \( S^1 \to S^1 \) is not nullhomotopic, as the induced map of fundamental groups is the identity \( \pi_1(S^1) \to \pi_1(S^1) \). In other words, \( S^1 \) is not contractible.

Corollary. There are no retractions \( B^2 \to S^1 \), as a retraction is merely the extension of the identity on \( S^1 \) to all of \( B^2 \).

Corollary. The inclusion \( i: S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\} \) is not nullhomotopic, as there is a retraction \( r: \mathbb{R}^2 \setminus \{0\} \to S^1 \) given by \( r(x) = x / \|x\| \). Since \( id_{\pi_1(S^1)} = r_* \circ i_* \) implies \( i_* \) is injective, the lemma implies \( i \) is not nullhomotopic.

The lemma packages the relationship between homotopy and extension into one result.

We are now poised to offer a different, perhaps more intuitive proof of the fixed point theorem.

Proof. Suppose for contradiction \( f: B^2 \to B^2 \) has no fixed points. Define \( g: B^2 \to \mathbb{R} \setminus \{0\} \) by \( g(x) = x - f(x) \). The restriction \( g|_{S^1} \) is a continuous map that extends to \( B^2 \), and is hence nullhomotopic by the lemma. On the other hand, we also claim it is homotopic to the inclusion \( i: S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\} \).

For \( x \in S^1 \), we have that \( x - f(x) \in \overline{B}_1(x) \setminus \{0\} \), which is a convex subset of \( \mathbb{R}^2 \). The straight line homotopy \( G(x, t) = x - (1 - t)f(x) \) doesn't intersect the origin. This is a contradiction, so \( f \) has a fixed point.

We will state the Borsuk-Ulam theorem in dimension 2.

Theorem. Let \( f: S^2 \to \mathbb{R}^2 \) be a continuous map. Then there exists \( x \in S^2 \) such that \( f(x) = f(-x) \).

87

<!-- page 88 -->

# 11/11/2019 - Antipodes and the Borsuk-Ulam Theorem

We spent some time last lecture proving the following result.

**Theorem.** *The following are equivalent.*

1. The map $h : S^1 \to X$ is nullhomotopic.
2. $h : S^1 \to X$ extends to a map $\overline{h} : B^2 \to X$.
3. The induced homomorphism $h_* : \pi_1(S^1, b_0) \to \pi_1(X, x_0)$ is trivial.

We saw that this result implies there is no retraction from $B^2$ to $S^1$. Brouwer's fixed point theorem, which says that every map $f : B^2 \to B^2$ admits a fixed point $f(x) = x$, then follows from this corollary.

The *Borsuk-Ulam theorem* is a result of a similar flavor.

**Theorem.** *Let $f : S^2 \to \mathbb{R}^2$ be continuous. Then there exists $x \in S^2$ such that $f(x) = f(-x)$.*

An analogous result holds for maps on the $n$-sphere $S^n \to \mathbb{R}^n$, but this requires more homotopy theory to prove. The case when $n = 1$ can be proven with the intermediate value theorem.

**Definition.** *The antipode of $x \in S^n$ is $-x \in S^n$. A map $h : S^n \to S^n$ is antipode-preserving if $h(-x) = -h(x)$.*

### Example

- The rotation of $S^1$ by an angle $\theta$ is antipode-preserving.

The follow result says something about the homotopy class of an antipode preserving map on the sphere.$^{43}$

**Theorem.** *If $h : S^1 \to S^1$ is continuous and antipode-preserving, then $h$ is not nullhomotopic.*

*Proof.* We will show that the induced $h_* : \pi_1(S^1) \to \pi_1(S^1)$ is nontrivial. If $[g] \in \pi_1(S^1)$ is a generator, $h_*$ takes $[g]$ to an odd multiple of $[g]$.

Let $\alpha : S^1 \to S^1$ be the antipodal map $\alpha(x) = -x$. The semicircle path $f : I \to S^1$ given by $f(s) = (\cos \pi s, \sin \pi s)$ goes from $b_0$ to $-b_0$. Then $g = f * (\alpha \circ f)$. Now, $h \circ f : I \to S^1$ is a path from $h(b_0)$ to $h(-b_0) = -h(b_0)$ and $h \circ (\alpha \circ f) = \alpha \circ h \circ f$ is a path from $-h(b_0)$ to $h(b_0)$ (as $h$ and $\alpha$ commute by assumption). The goal will then be to show $h_*(g) = (h \circ f) * (\alpha \circ h \circ f)$.

Let $p : \mathbb{R} \to S^1$ be the usual covering map of the circle. Choose a lift $t_0$ of $h(b_0)$. The lift $k$ of $h \circ f$ starting at $t_0$ ends at a point of $p^{-1}(-h(b_0)) = t_0 + 1/2 + \mathbb{Z}$. Let $t_0 + 1/2 + n$ be the endpoint. The

$^{43}$We present a concrete proof for the case $n = 1$. There is a more abstract proof in Munkres that generalizes this to other dimensions, using the fact that $S^n$ is the two-fold cover of projective space $\mathbb{R}P^n$.

88

<!-- page 89 -->

lift of $\alpha \circ h \circ f$ starting at $t_0 + 1/2 + n$ is then $\ell : I \to \mathbb{R}$ defined by $\ell(s) = k(s) + 1/2 + n$. This ends at $(t_0 + 1/2 + n) + 1/2 + n = t_0 + (2n + 1)$. Then $k * \ell : I \to \mathbb{R}$ is the lift of $h \circ g = h \circ f * (\alpha \circ h \circ f)$. It begins at $t_0$ and ends at $t_0 + 2n + 1$, which implies $h_*([g])$ is nontrivial.

**Corollary.** *There is no continuous antipode-preserving map $g : S^2 \to S^1$.*

*Proof.* Suppose for contradiction there exists such a $g : S^2 \to S^1$. By embedding $S^1 \subset S^2$ as the equator, we can view $g$ as a map $S^2 \to S^2$. Since $g$ is not surjective (its image lies on the equator), $g$ is nullhomotopic.

More explicitly, we can consider the restriction $g|_{S^1} \to S^2$. $g|_{S^1}$ extends to a map of the disc $B^2$ by embedding the disc as the upper hemisphere of $S^n$.

We can now prove the *Borsuk-Ulam theorem* in dimension 2.

**Theorem.** *Let $f : S^2 \to \mathbb{R}^2$ be continuous. Then there exists $x \in S^2$ such that $f(x) = f(-x)$.*

*Proof.* Suppose for contradiction there exists a $f : S^2 \to \mathbb{R}^2$ such that $f(x) \neq -f(-x)$ for all $x \in S^2$. Define $g : S^2 \to S^1$ by

$$g(x) = \frac{f(x) - f(-x)}{\|f(x) - f(-x)\|}$$

$g$ is clearly antipode-preserving, which is a contradiction.

A corollary is the *invariance of domain* when $n = 2$.

**Corollary.** *An open set in $\mathbb{R}^2$ is not homeomorphic to an open set of $\mathbb{R}^n$, where $n \geq 3$.*

Invariance of domain in dimension 1 is easy, as an open set of $\mathbb{R}^1$ can be separated removing a point, while open sets of $\mathbb{R}^n$ with $n \geq 2$ cannot be disconnected by removing a single point.$^{44}$

*Proof.* Let $U \subset \mathbb{R}^n$ be open, with $n \geq 3$. Suppose for contradiction there is a homeomorphism $f : U \to V \subset \mathbb{R}^2$. There is a closed ball $B_r(x) \subset U$ for small $r > 0$, on which the boundary $f : S^2 \to \mathbb{R}^2$ is continuous and injective, which contradicts Borsuk-Ulam theorem.

There is another amusing application of the Borsuk-Ulam. Given a sufficiently nice bounded subset $A \subset \mathbb{R}^2$, there exists a straight line in $\mathbb{R}^2$ that bisects $A$ into two pieces of equal area. The following theorem generalizes this.

**Theorem.** *Given sufficiently nice$^{45}$ bounded subsets $A_1, A_2 \subset \mathbb{R}^2$, there exists a straight line in $\mathbb{R}^2$ that simultaneously bisects both $A_1$ to $A_2$ into two pieces of equal area.*

$^{44}$The general result can be proven using *homology*.

$^{45}$These subsets should be measurable.

89

<!-- page 90 -->

Proof. View $A_1$ and $A_2$ as lying in the plane $\mathbb{R}^2 \times \{1\} \subset \mathbb{R}^3$. Given a point $u \in S^2 \subset \mathbb{R}^3$, let $P \subset \mathbb{R}^3$ be a plane through the origin with normal vector $u$. $P$ divides $S^3$ into two half-spaces. For all but the two vertical choices for $u$, $P$ divides the plane $\mathbb{R}^2 \times \{1\}$ into two pieces.$^{46}$ Define $f_i(u)$ to be the area of the part of $A_i$ that lies on the side of the normal vector $u$.

The functions $f_1, f_2 : S^2 \to \mathbb{R}$, are continuous and yield a continuous map $(f_1, f_2) : S^2 \to \mathbb{R}^2$. Furthermore, we clearly have $f_i(u) + f_i(-u) = \text{Area}(A_i)$. The Borsuk-Ulam implies there exists $u \in S^2$ such that $f_i(-u) = f_i(u) = \text{Area}(A_i)/2$. $\square$

Again, there is a generalization of this result to $n$ bounded, measurable regions in $\mathbb{R}^n$. There exists a hyperplane cut that simultaneously bisects all these regions. When $n = 3$, this is the ham-sandwich theorem, as it says that two pieces of bread and a slice of ham can be simultaneously bisected by a single hyperplane.$^{47}$

$^{46}$Here we are cleverly parameterizing the possible cuts of the plane $\mathbb{R}^2 \times \{1\}$ via the sphere. If a line is of the form $ax + by + c = 0$, we can normalize the vector $(a, b, c)$ to obtain a parameterized family of lines in the plane. This is the above construction.

$^{47}$A physicist's proof of this would be to consider the centers of mass of each of the three objects and then take the hyperplane that intersects these three points.

90

<!-- page 91 -->

# 11/13/2019 - Deformation Retracts and Homotopy Equivalence

Today we will discuss deformation retracts and homotopy equivalence. We have seen that spaces that are homeomorphic share many topological properties, but it turns out that often spaces look very much alike without being precisely homeomorphic.

Recall that given a subspace $A \subset X$, a retraction is a continuous $r : X \to A$ such that the restriction $r|_A$ acts as the identity on $A$. In other words, if $i : A \hookrightarrow X$ is the inclusion that $r \circ i = \mathrm{id}_A$.

# Example

- The constant map $S^1 \to p$ to a point $p \in S^1$ is a retraction.
- Consider the unit sphere $S^n$. Then $S^n$ admits a retraction $S^n \to H$ onto the upper hemisphere $H = \{x_{n+1} \geq 0\}$ given by $(x_1, \ldots, x_{n+1}) \mapsto (x_1, \ldots, |x_{n+1}|)$.
- There is a retraction $\mathbb{R}^2 \setminus \{0\} \to S^1$ given by $x \mapsto x / \|x\|$.
- There is a retraction from the Möbius band onto its core circle $S^1$ obtained by projecting $I \times I / \sim$ to the first coordinate.

The second two examples are different from the first two, as one would like to argue that $\mathbb{R}^2 \setminus \{0\}$ and $S^1$ are the same in a way more fundamental then $S^1$ and $p$ are. Namely, all of the homotopy information of $\mathbb{R}^2 \setminus \{0\}$ is the same as that of $S^1$.

The idea is that it is possible to continuously deform the identity map on $\mathbb{R}^2 \setminus \{0\}$ to the retraction $r : \mathbb{R}^2 \setminus \{0\} \to S^1$. In other words, the identity map is homotopic to the retraction.

# Example

- Consider again the Möbius band $X = I \times I / (0, y) \sim (1, 1 - y)$ and the subspace $A = I \times \{1/2\} / (0, 1/2) \sim (1, 1/2)$. Define the homotopy

$$H : X \times I \to X$$

$$([x, y], t) \mapsto [x, t \frac{1}{2} + (1 - t)y]$$

The definition $((x, y), t) \mapsto (x, t/2 + (1 - t)y)$ is compatible with the equivalence relation $\sim$, so $H$ descends to a homotopy of the quotient.

Definition. A subspace $A \subset X$ is a deformation retract of $X$ if $\mathrm{id}_X$ is homotopic to a map $X \to A$ such that the points of $A$ are fixed throughout the homotopy. Explicitly, there exists a continuous $H \times I \to X$ such that

- $H(x, 0) = x$ for all $x \in X$
- $H(x, 1) \in A$ for all $x \in X$
- $H(a, t) = a$ for all $a \in A$ and all $t$

91

<!-- page 92 -->

$H$ is a deformation retraction.

Given a deformation retraction $H$, there is a retraction $r : X \to A$ given by defining $r(x) = H(x, 1)$. So being a deformation retract is a stronger condition than being merely a retract.

A deformation retract can also be stated as a retraction $r : X \to A$ along with a homotopy $H$ between $\mathrm{id}_X$ and $r$ that fixes points of $A$.

# Example

- The retraction $r : \mathbb{R}^n \setminus \{0\} \to S^{n-1}$ given by $x \mapsto x / \|x\|$ is homotopic to the identity on $\mathbb{R}^n \setminus \{0\}$ via the straight line homotopy. Define

$$H : X \times I \to X$$

$$(x, t) \mapsto t \frac{x}{\|x\|} + (1 - t)x$$

The straight line segment from $x$ to $x / \|x\|$ does not pass through the origin, so this is well-defined. $H$ also fixes $S^{n-1}$ throughout the homotopy.

The existence of a deformation retract allows us to say something about the homotopy of a space relative to its subspace. We've seen that if $A$ is a retract of $X$, then the induced $i_* : \pi_1(A) \to \pi_1(X)$ is injective and the induced $r_* : \pi_1(X) \to \pi_1(A)$ is surjective.⁴⁸ When $A$ is a deformation retract, this will become isomorphisms.

Proposition. Suppose $h, k : (X, x_0) \to (Y, y_0)$ are homotopic with the property that the homotopy preserves the base point. Then $h_* = k_*$.

Proof. Let $f$ be a loop in $(X, x_0)$. Then

$$I \times I \xrightarrow{f \times \mathrm{id}} (X, x_0) \times I \xrightarrow{H} (Y, y_0)$$

is a path homotopy between $h \circ f$ and $k \circ f$. Since the homotopy $H$ holds the base point constant, we know that this composition indeed defines a path homotopy that fixes endpoints. □

What happens in the base point during the homotopy does not stay fixed? If $h, k : X \to Y$ are homotopic with homotopy $H$ but $y_t = H(x_0, t)$ is not constant, let $\alpha(t) = y_t$ be a path from $y_0$ to $y_1$. We cannot say that $h_*$ and $k_*$ are equal, as they are maps to different groups:

$$h_* : \pi_1(X, x_0) \to \pi_1(Y, y_0)$$

$$k_* : \pi_1(X, x_0) \to \pi_1(Y, y_1)$$

There is an isomorphism between the two codomains induced by the path $\alpha$ defined by

$$\widehat{\alpha} : \pi_1(Y, y_0) \to \pi_1(Y, y_1)$$

$$[g] \mapsto [\alpha^{-1} * g * \alpha]$$

Then the correct conclusion is the following.

⁴⁸ As if $r \circ i = \mathrm{id}_A$, then $r_* \circ i_* = \mathrm{id}_{\pi_1(A)}^*$, which implies $i_*$ is injective and $r_*$ is surjective.

92

<!-- page 93 -->

**Theorem.** Given the above conditions, we have a commutative diagram

$$\pi_1(X, x_0) \xrightarrow{h_*} \pi_1(Y, y_0)$$
$$\downarrow_{\widehat{a}}$$
$$k_*$$
$$\pi_1(Y, y_1)$$

Proof. Let $F : I \times I \to X \times I$ be a path homotopy of loops based at $(x_0, 1)$ obtained by

- $(x_0, 1) \mapsto (x_0, t)$
- $f$ in $X \times \{t\}$
- $(x_0, t) \mapsto (x_0, 1)$

Now we can prove the following theorem.

**Theorem.** If $A \subset X$ is a deformation retract, then the inclusion $i : (A, x_0) \to (X, x_0)$ induces an isomorphism on fundamental groups.

Proof. Let $r : X \to A$ be a retraction and $H$ be a homotopy between $\mathrm{id}_X$ and $i \circ r$. As usual, the induced $i_*$ is injective. And since $i \circ r$ is homotopic to the identity, by the above proposition $i_* \circ r_* = \mathrm{id}_{\pi_1(X)}$, so $i_*$ is also surjective.

In conclusion, we don't need that two maps compose to the identity in order to induce an isomorphism on homotopy. It suffices that their composition is homotopic to the identity.

### Example

- $S^1$ has the same fundamental group as the cylinder $S^1 \times I$, the Möbius band $I \times I / \sim$, the punctured plane $\mathbb{R}^2 \setminus \{0\}$, the solid torus $S^1 \times B^2$.
- The figure eight space (wedge of two circles $S^1 \vee S^1$) is a deformation retract of $\mathbb{R}^2 \setminus \{1, -1\}$. The $\theta$-graph$^a$ is also a deformation retract of $\mathbb{R}^2 \setminus \{1, -1\}$. All three spaces have the same fundamental group, although the $\theta$-graph and $S^1 \vee S^1$ are not deformation retracts of each other.

$^a$It looks like a $\theta$ in the plane.

The second example illustrates that there is a more general relation between spaces than deformation retract. In fact, since we noticed that it suffices for $i \circ r$ to be homotopic to the identity, we might as well also allow $r \circ i$ to be homotopic to the identity, rather than demanding strict equality.

**Definition.** Let $f : X \to Y$ and $g : Y \to X$ be continuous maps. If $g \circ f : X \to X$ and $f \circ g : Y \to Y$ are both homotopic to the identity, then $f$ and $g$ are **homotopy equivalences**. In such a case, $X$ and $Y$ are **homotopy equivalent**. We say $X$ and $Y$ have the same **homotopy type**.

93

<!-- page 94 -->

Spaces of the same homotopy type are indistinguishable in algebraic topology.

### Example

- If $A$ is a deformation retract of $X$, then $A$ and $X$ have the same homotopy type and $i: A \hookrightarrow X$ and $r: X \to A$ are homotopy equivalences.
- The inclusion of the $\theta$-graph into $\mathbb{R}^2 \setminus \{1, -1\}$ and then the retraction onto $S^1 \vee S^1$ is a homotopy equivalence between the $\theta$-graph and $S^1 \vee S^1$. This is a particular case of the following proposition.

**Proposition.** If $f: X \to Y$ and $g: Y \to Z$ are homotopy equivalences, then $g \circ f: X \to Z$ is a homotopy equivalence.

A homotopy inverse of $g \circ f$ is obtained by composing inverses for $f$ and $g$ in the opposite order.

**Theorem.** Let $f: (X, x_0) \to (Y, y_0)$ be a homotopy equivalence. The induced $f_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$ is an isomorphism.

The proof is similar to the case of deformation retracts with some additional details.

Proof. Let $g: Y \to X$ be a homotopy inverse to $f$ with $g(y_0) = x_1 \in X$. There is a composition

$$\pi_1(X, x_0) \xrightarrow{f_*} \pi_1(Y, y_0) \xrightarrow{g_*} \pi_1(X, x_1) \xrightarrow{f'_*} \pi_1(Y, y_1)$$

We know $g \circ f$ is homotopic to $\mathrm{id}_X$, so $g_* \circ f_* = \widehat{\alpha} \circ \mathrm{id}_{\pi_1(X, x_0)}$ where $\alpha$ is the path from $x_0$ to $x_1$ that arises from the homotopy from $\mathrm{id}_X$ to $g \circ f$. This implies $f_*$ is injective and $g_*$ is surjective.

$f \circ g$ is homotopic to the identity, so $f'_* \circ g_*$ is an isomorphism $\pi_1(Y, y_0) \to \pi_1(Y, y_1)$. This implies $g_*$ is injective and $f'_*$ is surjective. Thus $g_*$ is an isomorphism, which completes the proof.$^{49}$

$^{49}$This means that $\pi_1: \text{Top} \to \text{Grp}$ descends to a functor $\text{HoTop} \to \text{Grp}$.

94

<!-- page 95 -->

# 11/18/2019 - Computing the Fundamental Group

Broadly, we are attempting to develop tools to understand homotopy theory, which studies the space of maps between two spaces. We are focusing on the maps between the circle and and space, which is fundamental group.

Last lecture we introduced homotopy equivalence, which gives a more general notion of ‘same-ness’ for topological spaces. Homotopy equivalence is one way of determining when two spaces have the same fundamental group. Last group we proved the following result.

Lemma. Let \( f: X \to Y \) be a homotopy equivalence. Then the induced map \( f_{*}: \pi_{1}(X, x_{0}) \to \pi_{1}(Y, y_{0}) \) is an isomorphism.

So homotopy classes of maps from  \( S^{1} \)  to X and to Y behave the same way. In fact, homotopy classes of maps from any spaces into X and Y behave the same way. We will present a simplified, shorter proof of this result in a special case.

Proof. Suppose  \( f: X \to Y \)  is a homotopy equivalence that takes  \( f(x_{0}) = y_{0} \) . Assume the homotopy inverse  \( g: Y \to X \)  takes  \( g(y_{0}) = x_{0} \)  and the homotopies preserve basepoints. \( ^{50} \)  Then we have

![img-30.jpeg](img-30.jpeg)

Then a homotopy between \( g \circ f \) and id yields, for all loops \( h: I \to X \), a homotopy between \( (g \circ f) \circ h \) and \( h \).

This result gives access to many examples of spaces and their fundamental groups.

# Example

- Let \( A \subset X \) be a deformation retract. Then the inclusion \( i: A \hookrightarrow X \) and retraction \( r: X \to A \) are homotopy equivalences, so \( \pi_1(X) \simeq \pi(A) \).

Thus the cylinder \( S^1 \times I \), the Möbius band \( I \times I / (0, y) \sim (0, 1 - y) \), and the punctured plane \( \mathbb{R}^2 \setminus \{0\} \).

Note that if two spaces have the same fundamental group, they are not necessarily homotopy-equivalent. An easy example is the sphere \( S^2 \) and the point, although we don't have a way to show this.

The rest of the course will consist of studying ways to compute fundamental groups as well as what these have to tell us about homotopy theory.

\( ^{50} \) The lack of these assumptions is what makes the proof trickier in the general case.

95

<!-- page 96 -->

Given a decomposition $X = U \cup V$ into open subsets for which we know $\pi_1(U)$ and $\pi_1(V)$, what can we say about $\pi_1(X)$? For example, we can split $S^n$ into two hemispheres for which we know their fundamental groups. Can this tell us anything about the fundamental group of $S^n$?

Another example is the figure-eight space $S^1 \vee S^1$. There are open subsets that consist of each copy of $S^1$ and a bit of extra material. We know each of these is homotopy equivalent to $S^1$. So we know the fundamental group of the pieces. Do we know anything about the fundamental group of $S^1 \vee S^1$?

There is a general answer to this question, the Seifert van Kampen theorem. For simplicity, we will first present a simpler version of the result.

**Theorem.** Suppose $X = U \cup V$, with $U, V$ open and $U \cap V$ path-connected. Let $x_0 \in U \cap V$ be the basepoint, and let $i: U \hookrightarrow X$ and $j: V \hookrightarrow X$ be the inclusion maps. Then the images of the induced homomorphisms $i_*: \pi_1(U, x_0) \to \pi_1(X, x_0)$ and $j_*: \pi_1(V, x_0) \to \pi_1(X, x_0)$ generate $\pi_1(X, x_0)$.

When we say that a collection of elements generates a group, this means that the smallest subgroup that contains these elements is in fact the entire group. More concretely, every element of $\pi_1(X, x_0)$ can be expressed as the product of elements of the subgroups im $i_*$ and im $j_*$. This doesn't mean that every loop in $X$ lies in either $U$ or $V$, but instead that we can express any such loop as the product of loops that lie in either $U$ or $V$.

Proof. Let $f: I \to X$ be a loop based at $x_0$. We can pullback the open cover for a cover $[0, 1] = f^{-1}(U) \cup f^{-1}(V)$. By the Lebesgue number lemma, there exists $\delta > 0$ such that for any subinterval of $[0, 1]$ of length less than $\delta$, this subinterval lies completely in either $f^{-1}(U)$ or $f^{-1}(V)$. Then we can consider a finite subdivision $0 = a_0 < a_1 < \ldots < a_n = 1$ such that $f([a_i, a_{i+1}])$ lies in either $U$ or $V$. Without loss of generality, by combining subintervals if necessary, we can take these subintervals such that $f([a_i, a_{i+1}])$ alternates between lying in $U$ and $V$.

Let $f_i = f|_{[a_{i-1}, a_i]}$. Since the image of the subintervals $[a_{i-1}, a_i]$ alternates between lying in $U$ and $V$, we know $f(a_i) \in U \cap V$ for all $i$. Choose a path $\alpha_i$ in $U \cap V$ from $x_0$ to $f(a_i)$, and let $\alpha_0$ and $\alpha_n$ be constant paths at $x_0$. Then

$$f \simeq (\alpha_0 * f_1 * \alpha_1^{-1}) * (\alpha_1 * f_2 * \alpha_2^{-1}) * \ldots * (\alpha_{n-1} * f_n * \alpha_n^{-1})$$

where each $\alpha_{i-1} * f_i * \alpha_i^{-1}$ is a loop at $x_0$ contained in either $U$ or $V$.

**Corollary.** Suppose $X = U \cup V$, with $U, V$ open and simply connected and $U \cap V$ path connected. Then $X$ is simply connected.

Proof. $\pi_1(X)$ is generated by the images of trivial groups, so $\pi_1(X)$ is itself trivial.

**Corollary.** When $n \ge 2$, $\pi_1(S^n) = \{1\}$.

Proof. Let $S^n = U \cup V$, where $U = S^n \setminus \{(0, 0, \ldots, 1)\}$ and $V = S^n \setminus \{(0, 0, \ldots, -1)\}$. The claim is that $U$ and $V$ are both homeomorphic to $\mathbb{R}^n$. We can use stereographic projection. Place $S^n$ in $\mathbb{R}^{n+1}$ such that $\mathbb{R}^n \times \{0\} \subset \mathbb{R}^{n+1}$ intersects $S^n$ along the equator. Then for a point $Z \in U$, take

96

<!-- page 97 -->

the unique line through \(N\) and \(Z\). Then define \(f: U \to \mathbb{R}^n\) by taking \(z = f(Z)\) to be the unique intersection of this line and \(\mathbb{R}^n \times \{0\} \subset \mathbb{R}^{n+1}\).

![img-31.jpeg](img-31.jpeg)

The formula is

\[
f (z _ {1}, \ldots , z _ {n + 1}) = \left(\frac {z _ {1}}{1 - z _ {n + 1}}, \ldots , \frac {z _ {n}}{1 - z _ {n + 1}}\right)
\]

Hence \(U\) and \(V\) are simply connected. Since \(U \cap V \simeq \mathbb{R}^n \setminus \{0\}\) by the same technique\(^{51}\) if \(n \geq 2\), the theorem implies \(\pi_1(S^n) = \{1\}\).

# Computing the fundamental group of projective space

- The quotient of \( S^n \) by the relation \( \sim \) defined by \( x \sim -x \) is homeomorphic to \( \mathbb{R}P^n \). The map \( p: S^n \to S^n / \sim \simeq \mathbb{R}P^2 \) is a covering map of degree 2.

Since \( S^n \) is path connected and simply connected, the lifting correspondence \( \varphi : \pi_1(\mathbb{R}P^n) \to p^{-1}(b_0) \) is a bijection. The fibers of \( p \) have cardinality 2, which implies that \( \pi_1(\mathbb{R}P^2) \simeq \mathbb{Z}/2\mathbb{Z} \) is the unique group of order 2.

- Consider the figure-eight space \( S^1 \vee S^1 \) with the cover \( S^1 \vee S^1 = U \cup V \), where \( U \) and \( V \) each consist of a circle and a bit extra to make \( U \) and \( V \) open.

![img-32.jpeg](img-32.jpeg)

Then \(\pi_1(S^1 \vee S^1)\) is generated by images of the two maps \(\mathbb{Z} \to \pi_1(X)\), so every element of \(\pi_1(X)\) can be expressed as the product of \(a\) loops and \(b\) loops. However, we do not yet know whether or not there are relations between the homotopy classes of \([a]\) and \([b]\). In turns out the there will be no such relations, which implies that \(\pi_1(X)\) is the free group on two generators.

However, we can prove that \(\pi_1(X)\) is not abelian, namely \(ab \neq ba\). We can cover \(S^1 \vee S^1\)

\( ^{51} \) In fact,  \( U \cap V \)  is homotopy equivalent to  \( S^{n-1} \) , which can be used to construct an induction number to compute the higher homotopy and homology of spheres in algebraic topology.

97

<!-- page 98 -->

by the following construction

![img-33.jpeg](img-33.jpeg)

Beginning at the origin, the lift of the loop $a * b$ ends at $1 \times 0$. The lift of $b * a$ ends at $0 \times 1$. Since $a * b$ and $b * a$ lift to different points and are not path homotopic, they are not homotopic in $S^1 \vee S^1$.

Note that this cover cannot distinguish between $a * b * a^{-1}$ and $b * a * b^{-1}$.

The above example illustrates that a deeper understanding of covering spaces could shed light on the fundamental group.

98

<!-- page 99 -->

# 11/20/2019 - Equivalence of Covering Spaces and the Universal Cover

We will next explore a classification of covering spaces of a space. This will help us understand the fundamental group.

## Classification of covering spaces

Let $p : (E, e_0) \to (B, b_0)$ be a covering map. Assume $E$ and $B$ are path connected. What is the relationship between $\pi_1(E, e_0)$ and $\pi_1(B, b_0)$? Given this answer, we can develop a theory as to whether or not a space $E$ covers $B$.

Proposition. The homomorphism $p_* : \pi_1(E, e_0) \to \pi_1(B, b_0)$ induced by a covering map $p : E \to B$ is injective.

Proof. Since $p_*$ is a group homomorphism, it suffices to check that the preimage of the identity is the identity. Suppose $p_*([f]) = e_{b_0}$ for $[f] \in \pi_1(E, e_0)$. Then $[f \circ p]$ is homotopic to the constant loop. $f$ is a lift of $f \circ p$, and we can lift this homotopy to a homotopy from $f$ to the constant loop in $E$. □

Therefore every covering $p : E \to B$ with a choice of base points $(E, e_0)$ and $(B, b_0)$ yields a subgroup $H = p_*(\pi_1(E, e_0)) \subset \pi_1(B, b_0)$ that is isomorphic to $\pi_1(E, e_0)$.

This will lead to two key results.

1. The subgroup $H \subset \pi_1(B, b_0)$ determines the covering space up to equivalence. In other words, all the information about a covering space is encoded in this subgroup.
2. Given a sufficiently nice$^{52}$ space $B$, for every subgroup $H \subset \pi_1(B, b_0)$ there exists a covering space $p : E \to B$ with $H = p_*(\pi_1(E, e_0))$.

Definition. Let $p : E \to B$ and $p' : E' \to B$ be covering spaces. $E$ and $E'$ are equivalent as covering spaces of $B$ if there exists a homeomorphism $h : E \to E'$ such that $p = p' \circ h$.

![img-34.jpeg](img-34.jpeg)

The condition $p = p' \circ h$ says that $h$ should map $E$ to $E'$ in a way that respects their structure as covering spaces of $B$. For all $b \in B$, $h$ gives a bijection $p^{-1}(b) \to p'^{-1}(b)$ that varies continuously as $b$ changes. In other words, $h$ takes sheets of one covering to another covering in a consistent way.

$^{52}$$B$ should be path connected, locally path connected, and semi-locally simply connected (this means that every neighborhood of any point contains a neighborhood for which the inclusion into $B$ induces the trivial homomorphism of fundamental groups.

99

<!-- page 100 -->

### Example

- There are two coverings of $S^1$ given by

$$p : \mathbb{R} \to S^1$$

$$x \mapsto (\cos x, \sin x)$$

$$p' : \mathbb{R} \to S^1$$

$$x \mapsto (\cos(2\pi x), \sin(2\pi x))$$

Then these coverings are equivalent by the homomorphism $h : \mathbb{R} \to \mathbb{R}$ defined by $h(x) = 2\pi x$.

The goal today will be to prove the following result.

**Theorem.** If $E \to B$ and $E' \to B$ are two coverings of $B$ that correspond to the same subgroup of $\pi_1(B, b_0)$, then $E$ and $E'$ are equivalent.

To prove this, we will need to be able to lifts maps to a covering space more generally.

**Definition.** A space $X$ is **locally path connected** if for all $x \in X$ and all open $U \subset X$ containing $x$, there exists an open $V \subset X$ containing $x$ such that $U \cap V$ is path connected.

### Example

- The union of two disjoint discs is locally path connected, but it is not path connected.
- The collection of points $\{1/n : n \in \mathbb{N}\} \cup \{0\}$ is not path connected and not locally path connected, as no neighborhood of 0 does not contain another point in the set.
- The space

$$\left( \bigcup_{n \in \mathbb{N}} \{1/n\} \times \mathbb{R} \right) \cup (0 \times \mathbb{R}) \cup (\mathbb{R} \times 0)$$

is path connected, but it is not locally path connected.

**Lemma.** Let $p : E \to B$ be a covering. A loop $f$ in $(B, b_0)$ lifts to a loop in $(E, e_0)$ if and only if $[f] \in p_*(\pi_1(E, e_0)) \subset \pi_1(B, b_0)$.

*Proof.* Let $f$ be such a loop in $(B, b_0)$, and let $\widetilde{f}$ be its lift in $(E, e_0)$ that is a loop. By definition $p \circ \widetilde{f} = f$, so $p_*([\widetilde{f}]) = [f]$.

Now suppose $[f] = p_*([\widetilde{g}])$ for some loop $\widetilde{g}$ in $(E, e_0)$. Then $f$ and $g = p \circ \widetilde{g}$ are path homotopic. Lifting this path homotopy yields a path homotopy between $\widetilde{f}$ and $\widetilde{g}$. Since $\widetilde{g}$ is a loop, $\widetilde{f}$ is a loop as well.

We can now prove a lifting lemma that will be very useful in the theory of covering spaces.

100

<!-- page 101 -->

**Theorem.** Let $p : E \to B$ be a covering map with $p(e_0) = b_0$. Let $Y$ be path connected and locally path connected. Let $f : (Y, y_0) \to (B, b_0)$ be a continuous map. Then $f$ can be lifted to $\widetilde{f} : Y \to E$ such that $\widetilde{f}(y_0) = e_0$ if and only if $f_*(\pi_1(Y, y_0)) \subset p_*(\pi_1(E, e_0))$ as subgroups of $\pi_1(B, b_0)$. Furthermore, such a lift of $f$, if it exists, is unique.

$$\begin{array}{c} (E, e_0) \\ \xrightarrow{\widetilde{f}} \xrightarrow{\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{(}E, e_0\text{)} \\ (Y, y_0) \xrightarrow{\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{(}B, b_0\text{)} \end{array}$$

This theorem is a complete characterization of obstructions to lifting maps to the covering space.

*Proof.* Suppose $f$ admits a lift to $\widetilde{f} : Y \to E$. Then $f = p \circ \widetilde{f}$, and by functoriality of $\pi_1$ we have the diagram

$$\begin{array}{c} \pi_1(E, e_0) \\ \xrightarrow{\widetilde{f}_*} \quad \downarrow p_* \\ \pi_1(Y, y_0) \xrightarrow{\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{(}B, b_0\text{)} \end{array}$$

which immediately implies that the image of $f_*$ lies in the image of $p_*$.

Conversely, suppose $f_*(\pi_1(Y, y_0)) \subset p_*(\pi_1(E, e_0))$. Let $y_1 \in Y$ and let $\alpha$ be a path from $y_0$ to $y_1$. Lift $f \circ \alpha : I \to B$ to a path in $E$ starting at $e_0$. Then define $\widetilde{f}(y_1)$ to be the endpoint of this path. We must show that the resulting function $\widetilde{f}$ is both well-defined and continuous. Note that if a lift $\widetilde{f}$ exists, then it is unique. For any $y_1 \in Y$, a path from $f(y_0)$ to $f(y_1)$ lifts uniquely to $E$ and hence determines $\widetilde{f}(y_1)$.

We first show that this is well-defined. Let $\beta$ be another path from $y_0$ to $y_1$. Then $\alpha * \beta^{-1}$ is a loop in $(Y, y_0)$, and $f \circ (\alpha * \beta^{-1}) = (f \circ \alpha) * (f \circ \beta^{-1})$ is a loop in $(B, b_0)$. By assumption $f_*([\alpha * \beta^{-1}]) \in p_*(\pi_1(E, e_0))$, so the lemma implies that $f_*([\alpha * \beta^{-1}))$ lifts to a loop in $(E, e_0)$.

$f \circ \alpha$ lifts to a path beginning at $e_0$ at ending at $\widetilde{f}(y_1)$, and $(f \circ \beta)^{-1}$ lifts to a path beginning at $\widetilde{f}(y_1)$ and ending at $e_0$. Therefore $f \circ \beta$ lifts to a path beginning at $e_0$ and ending at $\widetilde{f}(y_1)$, which shows that $\widetilde{f}(y_1)$ is independent of the choice of path.

Finally, we show that $\widetilde{f}$ is continuous. It is enough to check $\widetilde{f}$ is continuous on a neighborhood of each $y_1 \in Y$. Let $U$ be a neighborhood of $f(y_1) \in B$. Since $Y$ is locally path connected, there is a neighborhood $W$ of $y_1$ with $W \subset f^{-1}(U)$. Let $V$ denote the slice of $E$ containing $\widetilde{f}(y_1)$. The restriction $p|_V : V \to U$ is a homeomorphism. Any point of $f(W)$ is connected to $f(y_1)$ via a path in $U$. Lifting this path to $V$ starting at $\widetilde{f}(y_1)$ is obtained by the inverse $(p|_V)^{-1}$. So

$$\widetilde{f}|_W = (p|_V)^{-1} \circ f$$

101

<!-- page 102 -->

which is the composition of continuous functions.

![img-35.jpeg](img-35.jpeg)

Theorem. Let \( p: E \to B \) and \( p': E' \to B \) be covering spaces, with \( p(e_0) = p'(e_0') = b_0 \). Suppose \( E, E' \), and \( B \) are all path connected and locally path connected. Then there is an equivalence of covering spaces \( h: E \to E' \) such that \( h(e_0) = e_0' \) if and only if the subgroups \( H = p_*(\pi_1(E, e_0)) \) and \( H' = p_*( \pi_1(E', e_0')) \) of \( \pi_1(B, b_0) \) are equal. Furthermore, if such an equivalence exists then it is unique.

Proof. If such an equivalence exists, by functoriality of \( h \) we have

\[
\begin{array}{c} \pi_ {1} (E, e _ {0}) \xrightarrow {h _ {*}} \pi_ {1} (E ^ {\prime}, e _ {0} ^ {\prime}) \\ \Biggl \downarrow_ {p _ {*}} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \pi_ {1} (B, b _ {0}) \end{array}
\]

Now suppose \( H = H' \). By the lifting lemma, there exist basepoint-preserving lifts

\[
\begin{array}{c} E \\ \Bigg \downarrow_ {k} \\ E \xrightarrow {h} B \\ E \xrightarrow {p} B \end{array}
\]

So \( k \circ h \) is a lift of \( p: E \to B \). However, the identity map id: \( E \to E \) is also a lift of \( p \), so by uniqueness of lifts \( k \circ h = \mathrm{id} \). A similar argument shows \( h \circ k = \mathrm{id} \), which proves that \( h: E \to E' \) is indeed a homeomorphism.

# Classifying covering spaces of the circle

- There is the \(k\)-sheeted covering \(p_k: S^1 \to S^1\) given by \(p_k(z) = z^k\), viewing \(S^1 \subset \mathbb{C}\) as the

102

<!-- page 103 -->

subset of complex numbers with norm 1. Then the map

$$(p_k)_*: \pi_1(S^1, e_0) \simeq \mathbb{Z} \to \mathbb{Z} \simeq \pi_1(S^1, b_0)$$

is multiplication by $k$, and the subgroup corresponding to $p_k$ is $k\mathbb{Z}$.

- The usual covering map $p_0: \mathbb{R} \to S^1$ corresponds to the trivial subgroup $\{0\} \subset \mathbb{Z}$.
- These are all of the subgroups of $\mathbb{Z}$, so every connected covering space of $S^1$ is equivalent to either $S^1$ under $p_k$ or $\mathbb{R}$.

Next time we will discuss how allowing the basepoint of the covering space to change affects this theorem. We will also define the *universal cover*, which is the covering space corresponding to the trivial subgroup.

103

<!-- page 104 -->

# 11/25/2019 - Universal Covering Spaces, Free Groups

Let $p : E \to B$ be a covering map. Recall that we obtain a subgroup

$$H = p_*(\pi_1(E, e_0)) \subset \pi_1(B, b_0)$$

that consists of loops in $(B, b_0)$ that lift to loops in $(E, e_0)$. We proved the following classification of covering spaces using the lifting lemma.

**Theorem.** Let $p : E \to B$ and $p' : E' \to B$ be covering maps with $E, E', B$ path connected and $p(e_0) = p'(e'_0) = b_0$. There is an equivalence

![img-36.jpeg](img-36.jpeg)

such that $h(e_0) = e'_0$ if and only if the induced subgroups $H$ and $H'$ are equal.

What if we do not require $h(e_0) = e'_0$? In general, adjusting the basepoint of the cover changes the induced subgroup of $\pi_1(B, b_0)$. This is because choosing a new basepoint in the covering space adjusts the fundamental group by conjugation.

Let $e_0, e_1 \in p^{-1}(b_0)$. Given a path $\widetilde{\alpha}$ in $E$ from $e_0$ to $e_1$, $\alpha = p \circ \widetilde{\alpha}$ is a loop in $(B, b_0)$. The induced isomorphism is

$$\widetilde{\alpha}_* : \pi_1(E, e_0) \to \pi_1(E, e_1)$$

$$[h] \mapsto [\widetilde{\alpha}^{-1} * h * \widetilde{\alpha}]$$

Then the corresponding subgroups of $\pi_1(B, b_0)$ are related by

$$p_* \circ \widetilde{\alpha}_* : p_*(\pi_1(E, e_0)) = H \longrightarrow H' = p_*(\pi_1(E, e_1))$$

$$[h] \longmapsto p_*([\widetilde{\alpha}^{-1} * h * \widetilde{\alpha}]) = [\alpha]^{-1} * [p \circ h] * [\alpha]$$

This shows that $H$ and $H'$ are related by conjugation by $[\alpha]$, so $H$ and $H'$ are conjugate subgroups.

Conversely, given two conjugate subgroups $H_0 = p_*(\pi_1(E, e_0))$ and $H_1$ of $\pi_1(B, b_0)$ related by $H_1 = [\alpha]^{-1}H_0[\alpha]$, then lift $\alpha$ to a path $\widetilde{\alpha}$ in $E$ starting at $e_0$ and ending at $e_1$. Then we have $H_1 = p_*(\pi_1(E, e_1))$. This leads to the following more general classification result.

**Theorem.** Let $p : E \to B$ and $p' : E' \to B$ be path connected covering spaces. $E$ and $E'$ are equivalent if and only if the subgroups $H = p_*(\pi_1(E, e_0))$ and $H = p'_*(\pi_1(E', e'_0))$ are conjugate in $\pi_1(B, b_0)$

At this point we have produced some classification results for covering spaces. We will briefly discuss construction of covering spaces. Every fundamental group has a subgroup that is equal to the entire group. This corresponds to the trivial cover of a space by itself. However, every fundamental group also has the trivial group as a subgroup, which corresponds to the universal covering space.

104

<!-- page 105 -->

**Definition.** A *universal covering space* is a covering space $p : E \to B$ such that $E$ is simply connected.

The corresponding subgroup of a universal covering space is trivial.

**Remark.** By the previous theorem, universal covering spaces are unique up to equivalence.

### Examples

- The usual map $\mathbb{R} \to S^1$ is the universal cover.
- The product $p \times p : R \times R \to S^1 \times S^1$ is the universal cover.
- The universal cover of the figure-eight space $S^1 \vee S^1$ is the *Cayley graph on two generators*:

![img-37.jpeg](img-37.jpeg)

Since the universal covering space is simply connected, we have seen that the lifting correspondence $\pi_1(B, b_0) \to p^{-1}(b_0)$ is a bijection. The following theorem explains why such a cover is called *universal*.

**Theorem.** Let $p : E \to B$ be a universal covering space and $p' : E' \to B$ any path connected covering space. Then there exists a covering map $q : E \to E'$ such that $p' \circ q = p$, and $E$ is the universal covering space of $E'$.

![img-38.jpeg](img-38.jpeg)

Then we have the following result, which follows from the fact that covering maps are also quotient maps.

**Corollary.** Any path connected covering of $B$ can be realized as the quotient of the universal covering space.

### Not all spaces admit a universal covering spaces

- The *Hawaiian earring* space is given by the union

$$H = \bigcup_{n \ge 1} C_n \subset \mathbb{R}^2$$

105

<!-- page 106 -->

where $C_n$ is the circle of radius $1/n$ centered at $(1/n, 0)$.

![img-39.jpeg](img-39.jpeg)

Any covering map must evenly cover some neighborhood of the origin 0. This means for large enough $n$, the loop around $C_n$ lifts to a loop in the covering space, so no covering space of $H$ is simply connected.

Ruling out some pathological spaces yields the following existence result.

**Proposition.** *Suppose $B$ is locally simply-connected.*$^{53}$ *Then $B$ admits a universal covering space.*

*Proof.* Homotopy classes of loops should correspond to distinct sheets of the covering spaces, so that no loops in $(B, b_0)$ lift to a loop in $(E, e_0)$. So the fiber above a point $b \in B$ must consist of all possible paths from $b_0$ to $b_1$ up to homotopy. Then the idea is to build a universal cover of $B$ out of pairs $(b, [\gamma])$ for $b \in B$ and $[\gamma]$ a homotopy class of paths from $b_0$ to $b$.

At this point, $\{(b, [\gamma])\}$ is merely a set. There is a natural topology on $\{(b, [\gamma])\}$ obtained by using local simply connectedness. It is then straightforward to confirm that this is a covering space.

To obtain other covering spaces, one then simply restricts attention to certain homotopy classes of paths in this construction.

### Free groups

The other main tool to compute the fundamental group is Van Kampen's theorem. Today we will discuss *free groups* and *free products* and relate them to this theorem next week.

Let $G$ be a group, and let $G_1, \ldots, G_n$ be a collection of subgroups that *generate* $G$.$^{54}$ In general, the expressions for $g \in G$ are far from being unique. Further assume that $G_i \cap G_j$ is trivial for all $i \neq j$.

If $x = x_1 \ldots x_m$, then $(x_1, \ldots, x_m)$ is a *word* that represents $x$. There can be many words that represent $x$, as adding identity elements has no bearing on the product.

$^{53}$In fact, it suffices to assume $B$ is semi-locally simply connected, which means that every point has a neighborhood for which the inclusion into the whole space induces the trivial homomorphism on fundamental groups.

$^{54}$This means any $g \in G$ can be written as a product of elements in $G_1, \ldots, G_n$.

106

<!-- page 107 -->

A word is **reduced** if no $G_j$ contains consecutive $x_i$ and $x_{i+1}$. This implies that the identity is not present in the word, and that every $x_i$ is in a distinct subgroup $G_j$.

**Definition.** $G$ is the (internal) **free product** of its subgroups $G_1, \ldots, G_n$, denoted $G_1 * \ldots * G_n$, if

1. $G_1, \ldots, G_n$ generate $G$
2. $G_i \cap G_j = \{1\}$ for all $i \neq j$
3. For all $x \in G$, there is a unique reduced word that represents $x$.

The third condition is saying that there are no relations between elements in different subgroups.

### Example

- $\mathbb{Z}^2$ is *not* the free product of $\mathbb{Z}$ and $\mathbb{Z}$. $a + b = b + a$, as $\mathbb{Z}^2$ is abelian, so this element is represented by $(a, b)$ and $(b, a)$ (and $(a^2, b, a^{-1})$ along with many others).

**Definition.** The (external) free product of a collection of groups $G_1, \ldots, G_n$ is a group $G$ along with injective homomorphisms $i_j : G_j \to G$ such that $G = i_1(G_1) * \ldots * i_n(G_n)$.

The free product of groups always exists. It can be constructed as the set of reduced words in $G_1, \ldots, G_n$. The product is given by composition/concatenation of words.

**Remark.** The free product of groups is unique up to isomorphism, as since every element has a unique reduced word, this yields an isomorphism with the above concrete construction.

The free product of groups satisfies a *universal property*.

**Lemma.** Let $G = G_1 * \ldots * G_n$. For every group $H$ and collection of homomorphisms $h_j : G_j \to H$, there exists a unique homomorphism $h : G \to H$ such that $h = h_j \circ i_j$.

![img-40.jpeg](img-40.jpeg)

*Proof.* For an element $x = x_1 \ldots x_n$, let $h(x) = h(x_1) \ldots h(x_n)$. If $x_i \in G_j$, then define $h(x_i) = h_j(x_i)$.⁵⁵

**Definition.** The **free group** on elements $\{a_j\}$ is defined to be the free product of $G_j = \{a_j^n : n \in \mathbb{Z}\} \simeq \mathbb{Z}$.

⁵⁵This can always be written for a collection of groups that generate $G$, but it is not well-defined unless we have that $G$ is the free product. Uniqueness of the reduced word allows us to choose a preferred representative on which to define $h$.

107

<!-- page 108 -->

The free group on elements $\{a_j\}$ is thus the collection of all words with all possible exponents on each letter.

Returning to topology, we have seen that if $X = U \cup V$ with $U, V \subset X$ open and $U \cap V$ path connected, then $\pi_1(X, x_0)$ is generated by the subgroups $i_*(\pi_1(U, x_0))$ and $j_*(\pi_1(V, x_0))$, where $i$ and $j$ are the inclusions of $U$ and $V$, respectively. By the above universal property, there is a unique homomorphism

$$h : \pi_1(U, x_0) * \pi_1(V, x_0)$$

that agrees with $i_*$ and $j_*$. The weak version of Van Kampen's theorem implies that this homomorphism is a surjection. We adduce an additional result.

**Theorem.** *If $U \cap V$ is simply connected then the above map $h$ is an isomorphism.*

# Example

- The fundamental group of the figure-eight space $S^1 \vee S^1$ is the free group $\mathbb{Z} * \mathbb{Z}$.

108

<!-- page 109 -->

# 12/2/2019 - Seifert-Van Kampen Theorem, Final Examples

Today we will state the Seifert-Van Kampen theorem. This theorem provides a way to understand the fundamental group of a space $X = U \cup V$ in terms of the fundamental group of two open sets $U, V$.

First, we proved that in such a case the fundamental group of $X$ is generated by the images of the fundamental groups of $U$ and $V$ under the induced homomorphisms that arise from the inclusions $U \hookrightarrow X$ and $V \hookrightarrow X$.

Second, we stated that if $U \cap V$ is in fact simply connected then the fundamental group of $X$ is the free product of the fundamental groups of $U$ and $V$.

The Seifert-Van Kampen theorem addresses this question in its greatest generality. There is a diagram of inclusions of topological spaces

![img-41.jpeg](img-41.jpeg)

By the functoriality of $\pi_1$ we have a diagram

![img-42.jpeg](img-42.jpeg)

where $*$ indicates the free product$^{56}$ and the map $h$ is induced by the universal property of the free product.$^{57}$ Then from this perspective, the first statement above implies that $h$ is surjective. When $U \cap V$ is simply connected, the second statement above implies that $h$ is injective. The Seifert-Van Kampen theorem says something about the kernel of $h$ in the general case.

Theorem. Let $X = U \cup V$, where $U, V \subset X$ are open and $U \cap V$ is path connected. Then the natural homomorphism

$$h : \pi_1(U, x_0) * \pi_1(V, x_0) \to \pi_1(X, x_0)$$

extending $(j_1)_*$ and $(j_2)_*$ is surjective, and its kernel $N$ is the smallest normal subgroup$^{58}$ of $\pi_1(U, x_0) * \pi_1(V, x_0)$ which contains all elements of the form $(i_1)_*(g)^{-1}(i_2)_*(g)$ for all $g \in \pi_1(U \cap$

$^{56}$The free product of $G$ and $H$ can be explicitly constructed as the set of all words in $G$ and $H$, which are finite sequences of elements in $G$ and $H$, where no successive elements lie in the same group. The multiplication law in $G * H$ is given by composition of these words.

$^{57}$See the notes from last lecture.

$^{58}$We cannot simply consider the subgroup of elements of this form, as the quotient of a group by an arbitrary subgroup is only in general a set. To obtain another group, we must consider the normal closure, namely the smallest normal subgroup containing it, to obtain a quotient group.

109

<!-- page 110 -->

$V, x_0$). In other words, we have

$$\pi_1(X, x_0) \simeq (\pi_1(U, x_0) * \pi_1(V, x_0))/N$$

Taking the quotient by $N$ serves to identify the loops in $X$ that in fact arise from the same loops in $U$ and $V$. So $\pi_1(X)$ is the 'free-est' group that comes from $\pi_1(U)$ and $\pi_1(V)$ once we have identified the loops that lie in $U \cap V$.

**Corollary.** If $U \cap V$ is simply connected, then $N = \{1\}$ and $\pi_1(X, x_0) \simeq \pi_1(U, x_0) * \pi_1(V, x_0)$.

**Corollary.** If $V$ is simply connected, then $\pi_1(X, x_0) \simeq \pi_1(U, x_0)/N$, where $N$ is the smallest normal subgroup containing the image of $(i_1)_*: \pi_1(U \cap V, x_0) \to \pi_1(U, x_0)$.⁵⁹

### Examples

- Consider the figure-eight space $X$, which is the *wedge of two circles*.

![img-43.jpeg](img-43.jpeg)

Let $U$ be the left circle, along with a bit of the right circle so that it is open. Similarly let $V$ be the right circle. Both $U$ and $V$ deformation retract onto $S^1$, and $U \cap V$ is simply connected (it is contractible). The corollary then implies

$$\pi_1(X) \simeq \pi_1(S^1) * \pi_1(S^1) \simeq \mathbb{Z} * \mathbb{Z}$$

- Similarly, an easy inductive argument implies that the *wedge of $n$ circles* $X = \bigvee^n S^1$ has fundamental group

$$\pi_1(X) \simeq \underbrace{\mathbb{Z} * \ldots * \mathbb{Z}}_{n \text{ times}}$$

For example, the case when $n = 4$ is below.

![img-44.jpeg](img-44.jpeg)

⁵⁹We cannot say $\pi_1(U \cap V, x_0)$ is a subgroup of $\pi_1(U, x_0)$, as it is possible that the homomorphism $(i_1)_*$ is not even injective. Furthermore, there is no reason that the image should be normal.

110

<!-- page 111 -->

**Remark.** *Any connected finite graph$^{a}$ has the homotopy type of a wedge of finitely many circles.*

Although we won't prove this formally, the idea is simply that taking the quotient by an edge that connects two distinct vertices is a homotopy equivalence, so we can reduce the graph to having one vertex and many edges from that vertex to itself. Thus the fundamental group of any finite graph is a free group.

This implies that any subgroup of a free group is free, as such a subgroup corresponds to a covering space, and a covering space of a finite graph is also a graph.

$^{a}$In topology, a graph is a union of intervals glued at their endpoints.

### Fundamental groups of surfaces

- Consider the torus $T = S^1 \times S^1$. We can obtain the torus as the quotient $I \times I / \sim$, where $(x, 0) \sim (x, 1)$ and $(0, y) \sim (1, y)$.

![img-45.jpeg](img-45.jpeg)

Let $p = (1/2, 1/2)$ be the center of this square. Take $U = T \setminus \{p\}$ and $V$ a small disc centered at $p$.

$U$ deformation retracts to onto the figure-eight space via a radial deformation retract onto the boundary of the square, and then applying the identifications indeed yields the wedge of two circles (the figure-eight space). So $\pi_1(U, x_0) \simeq \mathbb{Z} * \mathbb{Z}$. $V$ is contractible, so $\pi_1(V, x_0)$.

The theorem implies $\pi_1(T) \simeq \pi_1(U)/N$, where $N$ is the smallest normal subgroup containing $(i_1)'_*(\pi_1(U \cap V))$. $U \cap V$ is the punctured disc, and it is homotopy equivalent to $S^1$ with fundamental group $\pi_1(U \cap V) \simeq \mathbb{Z}$. We must examine the image of a generator $f \in \pi_1(U \cap V)$ under $(i_1)_*$.

Following $f$ along the radial projection to the boundary and the identification of the edges illustrates that the image of $f$ under $(i_1)_*$ is $aba^{-1}b^{-1}$. Thus

$$\begin{aligned} \pi_1(T) &= (\mathbb{Z} * \mathbb{Z})/N \\ &= \langle a, b : ab = ba \rangle \\ &= \mathbb{Z} \times \mathbb{Z} \end{aligned}$$

as expected.

- We can similarly compute the fundamental group of the projective plane $\mathbb{R}P^2$. Recall

111

<!-- page 112 -->

that \(\mathbb{R}P^2\simeq S^2 /\sim\) , where \(\sim\) identifies antipodes \(x\sim -x\)

![img-46.jpeg](img-46.jpeg)

Then by restricting our attention to the upper hemisphere, we can also construct the projective plane as a quotient of the disc  \( RP^{2} \simeq B^{2}/\sim \) , where  \( \sim \)  identifies  \( x \sim -x \)  for  \( x \in S^{1} \)  and leaves points alone otherwise.

Let \( U = \mathbb{R}P^2 \setminus \{p\} \) and \( V \) be a small disc centered at \( p \). As in the previous example, \( \pi_1(V) \) is trivial. \( U \) deformation retracts onto \( S^1 / \sim \), which is itself homeomorphic to \( S^1 \). So \( \pi_1(U) \simeq \mathbb{Z} \). It remains to examine the image of \( \pi_1(U \cap V) \). \( U \cap V \) is homotopy-equivalent to \( S^1 \), so \( \pi_1(U \cap V) \). The generator of this group is sent along the radial retraction to the boundary, which is the loop that passes around the \( S^1 / \sim \) twice. Thus

\[
\pi_ {1} (\mathbb {R} P ^ {2}) \simeq \mathbb {Z} / 2 \mathbb {Z}
\]

- The Klein bottle can be constructed as the quotient \( I \times I / \sim \), where \( (x,0) \sim (x,1) \) and \( (0,y) \sim (1,1 - y) \).

![img-47.jpeg](img-47.jpeg)

Taking \( U = K \setminus \{p\} \) and \( V \) a small disc around \( p \) again yields \( \pi_1(U) \sim \mathbb{Z} * \mathbb{Z} \) and \( \pi_1(V) \) trivial by the same argument as the torus. \( U \cap V \) is homotopy equivalent to \( S^1 \), so let \( f \) be a generator of \( \pi_1(U \cap V) \). Taking \( f \) along the radial retraction and examining its image after the identification yields \( aba^{-1}b \). So

\[
\pi_ {1} (K) \simeq \langle a, b: a b a ^ {- 1} b = 1 \rangle
\]

The relation can equivalently be given by \( ab = b^{-1}a \), or \( aba^{-1} = b^{-1} \). So \( b \) is conjugate to \( b^{-1} \). This group contains an index 2 subgroup \( H \) generated by \( a^2 \) and \( b \). Then

\[
a ^ {2} b a ^ {- 2} = a (a b a ^ {- 1}) a ^ {- 1} = a b ^ {- 1} a ^ {- 1} = b
\]

So \(a^2\) and \(b\) commute. Thus \(H\simeq \mathbb{Z}\times \mathbb{Z}\).

112

<!-- page 113 -->

An index 2 subgroup corresponds to a degree 2 covering space. The claim is that the subgroup $H \subset \pi_1(K)$ corresponds to a covering map $T \to K$, where $T$ is the torus and $K$ is the Klein bottle.$^a$

$^a$ 'If you paint a Klein bottle, the paint forms a torus.' -D. Auroux

113
