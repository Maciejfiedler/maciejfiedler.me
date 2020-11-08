<template>
  <c-dark-mode>
    <c-box
      p="20px"
      w="100vw"
      h="100vh"
      mr="auto"
      ml="auto"
      bgImage="url('https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=jeremy-perkins-uhjiu8FjnsQ-unsplash.jpg')"
    >
      <c-box p="20px" bg="black" color="white" borderRadius="15px">
        <c-stack spacing="2" pr="20px" pl="20px">
          <c-heading as="h1" textAlign="center" color="#6a71dc" size="2xl"
            >Maciej Fiedler</c-heading
          >
          <br />
          <c-heading as="h2" size="xl" textAlign="center">Status:</c-heading>
          <c-code fontSize="40px" textAlign="center">Good </c-code>
          <!---inplement API request here --->
          <br />
          <c-heading as="h3" size="xl" textAlign="center">Interests:</c-heading>
          <c-heading as="h4" size="lg" textAlign="center" color="gray.400"
            >Linux, backend systems, astronomy, physics, music, Overwatch,
            computer science, building websites, Minecraft, Docker, learning new
            programming languages
          </c-heading>
          <!---inplement API request here --->
        </c-stack>
      </c-box>

      <c-image
        p="20px"
        w="300px"
        mr="auto"
        ml="auto"
        src="https://raw.githubusercontent.com/Maciejfiedler/maciejfiedler.me/main/Assets/Logo%20(high%20resolution).png"
        alt="Logo"
      />
      <c-button
        bg="gray.600"
        size="lg"
        color="white"
        variant="solid"
        left-icon="email"
        textAlign="center"
        role="Lead to Github Repository"
        >Github Repository</c-button
      >
    </c-box></c-dark-mode
  >
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
            'Maciej, Fiedler, Maciej Fiedler, personal website, me, nuxtjs, nuxt.js, flask, caddy, github, github repository, github repo, repository, repo, my website, open-source ',
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
