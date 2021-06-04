# Enriching Parliamentary Metadata with Wikidata/Wikipedia

## Intro
British parliamentary data aggregated in the PoliticalMashup project lacks many metadata in the period before 1935. This repo aims to add missing metadata. It is focused on appending information to ```<membership>``` tags in the PoliticalMashup speaker metadata. Every speaker can have multiple memberships (member of the House of Commons in a specific period, or a cabinet position). Because Wikidata contains data on the MPs during parliamentary periods, Wikidata information can be used to enrich the data.

I focus on parties, but because the Wikidata keys are present throughout the process all kinds of metadata can be added (birth date etc.)

## Steps

1. Scrape election results from Wikipedia (```s0_parse_wikipedia_data.ipynb```)
2. Download ```.tsv``` files for every election with the Wikidata query service. [This](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3FconstituencyLabel%20%3FpartyLabel%20%3Fstart%20%3FelectionLabel%20%3Fend%20%3FcauseLabel%20%7B%0A%20%3Fitem%20p%3AP39%20%3FpositionStatement%20.%0A%20%3FpositionStatement%20ps%3AP39%20wd%3AQ35494253%20.%20%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP768%20%3Fconstituency%20.%20%7D%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP4100%7Cpq%3AP102%20%3Fparty%20.%20%7D%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP580%20%3Fstart%20.%20%7D%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP2715%20%3Felection%20.%20%7D%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP582%20%3Fend%20.%20%7D%0A%20OPTIONAL%20%7B%20%3FpositionStatement%20pq%3AP1534%20%3Fcause%20.%20%7D%0A%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%27en%27%20%7D%0A%7D%0AORDER%20BY%20%3Fstart) is the query format.
3. Transform the downloaded Wikidata tables (```s1_transform_wikidata_tables.py```)
4. Add missing party data to Wikidata tables using the Wikipedia tables gathered in step 1 (```s2_add_parties_to_wikidata.ipynb```)
5. Flatten the ```.xml``` member data to ```.csv``` files (because ```.xml``` is horrible) (```s3_flatten_member_metadata.ipynb```)
6. Enrich the district/constituency metadata in the Wikidata tables (```s5_enrich_memberships.ipynb```). Fuzzy string matching is used to match districts. I correct this manually afterwards. This step is necessary because I use the districts/constituencies as a way to match speakers and parties later.
7. The final (not yet complete) step is to match all the enriched wikidata with the PoliticalMashup membership tags based on exact name matches, district and parliamentary dates matches and, if all else fails, fuzzy string matching. (```s6_add_party_to_memberships.ipynb```). As far as I can see the whole endeavour leads to 56% of the missing party data being found!