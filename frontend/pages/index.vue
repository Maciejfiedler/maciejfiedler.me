<template>
  <c-light-mode>
    <c-box p="20px" height="100vh" bg="green.50">
      <c-flex align="center" justify="center">
        <c-box p="20px" maxW="1000px">
          <c-stack spacing="2" pr="20px" pl="20px" textAlign="center">
            <c-heading as="h1" size="2xl">Maciej Fiedler</c-heading>
            <c-heading as="h2" size="xl">Status</c-heading>
            <c-code variant-color="green" fontSize="4xl">{{ myStatus }}</c-code>
            <br />
            <c-heading as="h2" size="xl">Description</c-heading>
            <c-text fontSize="xl">{{ myDescription }}</c-text>
            <br />
            <c-heading as="h2" size="xl">Interests</c-heading>
            <c-text fontSize="xl">{{ myInterests }}</c-text>
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
              fontSize="lg"
              href="https://www.instagram.com/maciej.me/"
              color="pink.400"
              role="Lead to Instagram Account"
              >Instagram</c-link
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
          <c-flex align="center" justify="center">
            <c-link
              textAlign="center"
              is-external
              role="Lead to my Email"
              fontSize="lg"
              href="mailto:maciek.fiedler@gmail.com"
              color="blue.400"
              >maciek.fiedler@gmail.com</c-link
            ></c-flex
          >
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
        </c-box></c-flex
      >
    </c-box></c-light-mode
  >
</template>

<script lang="ts">
/* eslint-disable vue/no-unused-components */
import Chakra from '@chakra-ui/vue'
import gql from 'graphql-tag'

export default {
  name: 'App',
  head() {
    return {
      title: "Maciej Fiedler's personal website.",
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'This website is a personal project to express myself. ',
        },
        {
          hid: 'keywords',
          name: 'keywords',
          content:
            'maciej fiedler personal website me nuxtjs nuxt.js flask caddy docker github repository repo my website open source ',
        },
        {
          hid: 'author',
          name: 'author',
          content: 'Maciej Fiedler ',
        },
      ],
    }
  },
  components: {
    Chakra,
  },
  async asyncData({ $strapi }: any) {
    const response = await $strapi.graphql({
      query: ` 
        query getPosts{
          posts{
            id
            title
            content
          }
        }`,
    })
    return response
  },
  apollo: {
    myStatus: gql`
      query getStatus {
        myStatus
      }
    `,
    myDescription: gql`
      query getDescription {
        myDescription
      }
    `,
    myInterests: gql`
      query getInterests {
        myInterests
      }
    `,
  },
}
</script>

<style>
body {
  background: #e2fbed;
}
</style>
