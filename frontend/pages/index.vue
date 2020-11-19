<template>
  <c-light-mode>
    <c-box p="20px" bg="blue.50">
      <c-flex align="center" justify="center">
        <c-box p="20px" maxW="1000px">
          <c-stack spacing="2" pr="20px" pl="20px" textAlign="center">
            <c-heading as="h1" size="2xl">Maciej Fiedler</c-heading>
            <c-heading as="h2" size="xl">Status</c-heading>
            <c-code variant-color="blue" fontSize="40px">{{ myStatus }}</c-code>
            <!-- inplement API request here -->
            <br />
            <c-heading as="h2" size="xl">Description</c-heading>
            <c-text fontSize="xl">{{ myDescription }}</c-text>
            <br />
            <c-heading as="h2" size="xl">Interests</c-heading>
            <!-- inplement API request here -->
            <c-text fontSize="xl">{{ myInterests }}</c-text>
            <!-- inplement API request here -->
          </c-stack>
          <br />
          <c-heading as="h2" size="xl" textAlign="center">Social</c-heading>
          <c-stack
            spacing="2"
            pr="20px"
            pl="20px"
            textAlign="center"
            justify="center"
            isInline
          >
            <c-link
              textAlign="center"
              is-external
              fontSize="lg"
              href="https://twitter.com/MaciejFiedlerOn"
              color="blue.400"
              role="Lead to Twitter Account"
              >Twitter</c-link
            >
            <c-link
              textAlign="center"
              is-external
              role="Lead to Github Account"
              fontSize="lg"
              href="https://github.com/Maciejfiedler"
              color="black"
              >Github</c-link
            >
          </c-stack>
          <br />
          <c-flex align="center" justify="center">
            <c-link
              bg="black"
              color="white"
              textAlign="center"
              role="Lead to Github Repository"
              is-external
              p="8px"
              rounded="5px"
              href="https://github.com/Maciejfiedler/maciejfiedler.me"
              >Github Repository</c-link
            >
          </c-flex>

          <c-image
            p="20px"
            w="600px"
            mr="auto"
            ml="auto"
            src="https://raw.githubusercontent.com/Maciejfiedler/maciejfiedler.me/main/Assets/Logo%20(high%20resolution).png"
            alt="Logo, a duck on a star background"
            role="Show the Logo of the page"
          /> </c-box
      ></c-flex> </c-box
  ></c-light-mode>
</template>

<script lang="js">
/* eslint-disable vue/no-unused-components */
import Chakra from '@chakra-ui/vue'
import gql from "graphql-tag";

export default {
  name: 'App',
  head() {
    return {
      title: "Maciej Fiedler's personal website.",
      meta: [
        {
          charset: 'UTF-8',
        },
        {
          name: 'description',
          content: 'This website is a personal project to express myself. ',
        },
        {
          name: 'keywords',
          content:
            'Maciej Fiedler personal website me nuxtjs nuxt.js flask caddy docker github repository repo my website open-source ',
        },
        {
          name: 'author',
          content: 'Maciej Fiedler ',
        },
      ],
    }
  },
  components: {
    Chakra,
  },
  inject: ['$chakraColorMode', '$toggleColorMode'],
  apollo: {
    myStatus: gql`query getStatus{
      myStatus
    }`,
    myDescription: gql`query getDescription{
      myDescription
    }`,
    myInterests: gql`query getInterests{
      myInterests
    }`,
  }
}
</script>
