<template>
  <c-light-mode>
    <c-box p="20px">
      <c-box p="20px">
        <c-stack spacing="2" pr="20px" pl="20px" textAlign="center">
          <c-heading as="h1" size="2xl">Maciej Fiedler</c-heading>
          <br />
          <c-heading as="h2" size="xl">Status:</c-heading>
          <c-code fontSize="40px">Good </c-code>
          <!---inplement API request here --->
          <br />
          <c-heading as="h3" size="xl">Interests:</c-heading>
          <c-heading as="h4" size="lg"
            >Linux, backend systems, astronomy, physics, music, Overwatch,
            computer science, building websites, Minecraft, learning new
            programming languages and technologies
          </c-heading>
          <!---inplement API request here --->
        </c-stack>
        <br />
        <c-flex align="center" justify="center">
          <c-link
            bg="black"
            color="white"
            textAlign="center"
            role="Lead to Github Repository"
            is-external
            p="16px"
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
        />
      </c-box> </c-box
  ></c-light-mode>
</template>

<script lang="ts">
/* eslint-disable vue/no-unused-components */

import Chakra from '@chakra-ui/vue'

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
}
</script>
