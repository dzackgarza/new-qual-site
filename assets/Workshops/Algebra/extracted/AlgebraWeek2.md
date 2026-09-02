# Algebra Qual Prep Week 2: Finite Group Theory

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2\
1 Week 2: Finite Groups 3\
1.1 Topics 3\
1.2 Exercises 4\
1.2.1 Warmup 4\
1.2.2 Group Actions 5\
1.2.3 Automorphisms . 5\
1.2.4 Series of Groups 6\
2 Qual Problems 6

## 1 Week 2: Finite Groups

See the Presentation Schedule

<table><tr><td>1.1</td></tr><tr><td>Topics</td></tr></table>

• Recognition of direct products and semidirect products

• Amalgam size lemma: # $H K = \# H \# K / \# ( H \cap K )$

• Group actions

– Orbit-stabilizer

– The class equation,

– Burnside’s formula

– Important actions

♦ Self-action by left translation (the left-regular action)

♦ The assignment $g \mapsto \psi _ { g } \in \operatorname { S y m } ( G )$ where $\psi _ { g } ( x ) : = g x$ is sometimes referred to as the Cayley representation in qual questions, or sometimes a permutation representation since $\operatorname { S y m } ( G ) \cong S _ { n }$ as sets where $n : = \# G$

♦ See the Strong Cayley Theorem

♦ Self-action by conjugation

♦ Action on subgroup lattice by left-translation

♦ Action on cosets of a fixed G/H by left-translation

• Transitive subgroups

– How these are related to Galois groups

• FTFGAG: The Fundamental Theorem of Finitely Generated Abelian Groups

– Invariant factors

– Elementary divisors

• Simple groups

• Automorphisms

– Inner automorphisms

– Outer automorphisms (not often tested directly)

– Characteristic subgroups (not often tested directly)

• Series of groups (not often tested)

– Normal series

– Central series

– The Jordan-Holder theorem

♦ Composition series

– Solvable groups

♦ Derived series

– Nilpotent groups

♦ Lower central series

♦ Upper central series

A remark: automorphisms and series of groups aren’t often directly tested on the qual, but are useful practice.
Simple/solvable groups do come up often.

## 1.2 Exercises

## 1.2.1 Warmup

• Show that if $H , K \leq G$ are subgroups and $H \in N _ { G } ( H )$ , then HK is a subgroup.

– Find a counterexample where $H \leq G , K$ is only a subset and not a subgroup, and HK fails to be a subgroup?

• Prove the “Recognizing direct products” theorem: if H, K are normal in G with $H \cap K = \emptyset$ and $H K = G ,$ , then $G \cong H \times K$

– Hint: write down a map $H \times K \to G$ and follow your nose!

– How can you generalize this to 3 or more subgroups?

• State definitions of the following:

– Group action

– Orbit

– Stabilizer

– Fixed points

• State the orbit-stabilizer theorem

• State the class equation.
Can you derive this from orbit-stabilizer?

• Show that the center of a p-group is nontrivial

• Important: Pick your favorite composite number $m = \prod p _ { i } ^ { e _ { i } }$ and classify all abelian groups of that order.

– Write their invariant factor decompositions and their elementary divisor decompositions.
Come up with an algorithm for converting back and forth between these.

• Prove that if $H \leq G$ is a proper subgroup, then G can not be written as a union of conjugates of H. - Use this to prove that if $G = { \mathrm { S y m } } ( X )$ is the group of permutations on a finite set X with $\# X = n$ , then there exists a $g \in G$ with no fixed points in X.

• Define what a composition series is, and state what it means for a group to be simple, solvable, or nilpotent.

– How are the derived and lower/upper central series defined?
What $\mathrm { t y p e ( s ) }$ of the groups above does each series correspond to?

## 1.2.2 Group Actions

• For each of the following group actions, identify what the orbits, stabilizers, and fixed points are.
If possible, describe the kernel of each action, and its image in Sym(X).

– G acting on $X = G$ by left-translation:

$$
g \cdot x : = g x
$$

– G acting on $X = G$ by conjugation:

$$
g \cdot x : = g x g ^ { - 1 }
$$

– G acting on its set of subgroups $X : = { \Big \{ } H { \Big | } H \leq G { \Big \} }$ by conjugation:

$$
g \cdot H : = g H g ^ { - 1 }
$$

– For a fixed subgroup $H \leq G$ , G acting on the set of cosets $X : = G / H$ by left-translation:

$$
g \cdot x H : = ( g x ) H
$$

• Suppose X is a $G \mathrm { - s e t }$ , so there is a permutation action of G on X. Let $x _ { 1 } , x _ { 2 } \in X$ , and show that the stabilizer subgroups $\operatorname { S t a b } _ { G } ( x _ { 1 } )$ , $\mathrm { S t a b } _ { G } ( x _ { 2 } ) \leq G$ are conjugate in G.

• Let $[ G : H ] = p$ be the smallest prime dividing the order of G. Show that H must be normal in G.

• Show that if G is an infinite simple group, then G can not have a subgroup of finite index.

Hint: use the left-regular action on cosets.

• Show that every subgroup of order 5 in $S _ { 5 }$ is a transitive subgroup.

## 1.2.3 Automorphisms

• How do you compute the totient $\varphi ( p )$ for p prime?
Or $\varphi ( n )$ for n composite?

• What is the order of ${ \mathrm { G L } } _ { n } ( \mathbb { F } _ { p } ) ?$

• Identify $\operatorname { A u t } ( \mathbb { Z } / p )$ and $\operatorname { A u t } ( \prod _ { i = 1 } ^ { n } \mathbb { Z } / p )$ for p a prime.

– Identify $\operatorname { A u t } ( \mathbb { Z } / n )$ for n composite.

• How many elements in $\operatorname { A u t } ( \mathbb { Z } / 2 0 )$ have order 4?

• Find two groups $G \not \cong H$ where $\operatorname { A u t } G \cong \operatorname { A u t } H$

• Let $H , K \leq G$ be subgroups with $H \cong K$ . Is it true that $G / H \cong G / K ?$

Hint: consider a group with distinct subgroups of order 2 whose quotients have order 4.

• Show that inner automorphisms send conjugate subgroups to conjugate subgroups.

• Show that for $n \neq 6 , \mathrm { A u t } ( S _ { n } ) = \operatorname { I n n } ( S ^ { n } )$

## 1.2.4 Series of Groups

• Determine all pairs $n , p \in \mathbb { Z } ^ { \geq 1 }$ such that $\mathrm { S L } _ { n } ( \mathbb { F } _ { p } )$ is solvable.

• If $\# G = p q$ , is G necessarily nilpotent?

Hint: consider $Z ( S _ { 3 } )$

• Show that if G is solvable, then G contains a nontrivial normal subroup.

– What does this mean on the Galois theory side?

Hint: consider the derived series.

## 2 Qual Problems

## 2.1 Fall 2019 #1

Let G be a finite group with n distinct conjugacy classes.
Let $g _ { 1 } \cdots g _ { n }$ be representatives of the conjugacy classes of G. Prove that if $g _ { i } g _ { j } = g _ { j } g _ { i }$ for all $i , j$ then G is abelian.

Relevant concepts omitted.

## 5.5 Spring 2018 #1

a. Use the Class Equation (equivalently, the conjugation action of a group on itself) to prove that any p-group (a group whose order is a positive power of a prime integer p) has a nontrivial center.

b. Prove that any group of order $p ^ { 2 }$ (where p is prime) is abelian.

c. Prove that any group of order $5 ^ { 2 } \cdot 7 ^ { 2 }$ is abelian.

d. Write down exactly one representative in each isomorphism class of groups of order $5 ^ { 2 } \cdot 7 ^ { 2 }$

## 3.3 Spring 2016 #5

Let G be a finite group acting on a set X. For $x \in X$ $G _ { x }$ be the stabilizer of x and $G \cdot x$ be the orbit of x.

a. Prove that there is a bijection between the left cosets $G / G _ { x }$ and $G \cdot x$

b. Prove that the center of every finite p-group G is nontrivial by considering that action of G on $X = G$ by conjugation.

## 3.5 Fall 2018 #2

a. Suppose the group G acts on the set X . Show that the stabilizers of elements in the same orbit are conjugate.

b. Let G be a finite group and let H be a proper subgroup.
Show that the union of the conjugates of H is strictly smaller than G, i.e.

$$
\bigcup _ { g \in G } g H g ^ { - 1 } \subsetneq G
$$

c. Suppose G is a finite group acting transitively on a set S with at least 2 elements.
Show that there is an element of G with no fixed points in S.

## 3.4 Fall 2017 #1

Suppose the group G acts on the set A. Assume this action is faithful (recall that this means that the kernel of the homomorphism from G to Sym(A) which gives the action is trivial) and transitive (for all a, b in A, there exists g in G such that $g \cdot a = b . )$

$a \in A$ $G _ { a }$ denote the stabilizer of a in G. Prove that for any $a \in A$

$$
\bigcap _ { \sigma \in G } \sigma G _ { a } \sigma ^ { - 1 } = \left\{ 1 \right\} .
$$

b. Suppose that G is abelian.
Prove that $| G | = | A |$ . Deduce that every abelian transitive subgroup of $S _ { n }$ has order n.

Needs some Sylow theory:

## 4.11 Fall 2019 #2

Let G be a group of order 105 and let $P , Q , R$ be Sylow 3, 5, 7 subgroups respectively.

a. Prove that at least one of Q and R is normal in G.

b. Prove that G has a cyclic subgroup of order 35.

c. Prove that both Q and R are normal in G.

d. Prove that if P is normal in G then G is cyclic.
