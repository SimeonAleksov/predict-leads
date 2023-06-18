# Customers identification


### Introduction


Purpose of this report is to determine common web elements that represent customers of companies.

Research website examples:

- https://amplitude.com
- https://www.pagerduty.com
- https://gusto.com
- https://www.rippling.com

## Research

We'll examine each website separately and determine common elements.
Keywords to look for: 
- Customers
- Partners
- Testimonials


#### Amplitude

Immediately after opening the website, we can see that they have a section with couple of partners. Nothing special here, we can grab these logos but this isn't very useful.
After inspecting the page a little bit, we can see that they have a navigation to: https://partnerships.amplitude.com/English/directory/.

After inspecting the page, we can see that the partners cards are grouped in a `<div class="partner-cards xxxhorizontal-card">`, we can use this in combination with pagination
and grab every customer name, logo, and link.

#### Pagerduty

Similar to Amplitude, Pageduty has a customers page, where they're listed as cards https://www.pagerduty.com/customers/.
This page does not use any pagination, just hidden cards.


#### Gusto


Gusto is not different than the last 2, Gusto has a https://gusto.com/customers and https://gusto.com/customers/reviews, assuming we're
not interesting in the latter, the customers page has a list of cards within a div.

#### Rippling

Same. Rippling customers page https://www.rippling.com/customers, has a grid div, and div element with the customer page.
We would need to separate scrape this to get the company name and image clearly.

## Findings
Common elements we can use

- H(1/2/3)
- P
- IMG
- A

Although not common between these websites, `<article>` element is used often. For websites that use this, we can have generic
scrapers to get this data.

## Additional data

- https://scale.com/
- https://www.deel.com/ 

Both of these websites use the `<article>` element, just different inner elements, with this info, 
the scraper can be very generic.

## Conclusion

The elements and the trees are very similar, we can probably use some generic scraping pattern where we 
search for the above element and save the needed data.