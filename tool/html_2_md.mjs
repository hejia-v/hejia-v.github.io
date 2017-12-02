import fs from 'fs'
import toMarkdown from 'to-markdown'

// https://github.com/domchristie/to-markdown

const html_2_markdown = function () {
    const buffer = fs.readFileSync('./tool/data/data.html')
    const htmlText = buffer.toString()
    // console.log(htmlText)


    let mdText = toMarkdown(htmlText)
    console.log(mdText)
    console.log(toMarkdown('<h1>Hello world!</h1>'))

}


html_2_markdown()