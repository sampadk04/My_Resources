from jinja2 import Template

janapith_data = [
    {"year": 1965, "awardees": "G. Sankara Kurup", "language": "Malayalam"},
    {"year": 1966, "awardees": "Tarashankar Bandopadhyaya", "language": "Bengali"},
    {
        "year": 1967,
        "awardees": "Kuppali Venkatappagowda Puttappa",
        "language": "Kannada",
    },
]


# Read the template file content into a variable
template_file = open("janapith.html.jinja2")
TEMPLATE = template_file.read()
template_file.close()

# Render the template using Jinja2
template = Template(TEMPLATE)
content = template.render(janapith_data=janapith_data)

# Save the rendered html document
my_html_document_file = open("janapith.html", "w")
my_html_document_file.write(content)
my_html_document_file.close()


"""
This is how 'janapith.html.jinja2' file will look like.

<!DOCTYPE html>
<head>
        <meta charset="UTF-8"/>
        <title> Jnanpith </title>
        <meta name="description" content="This page lists Jnanpith Awardees"/>
</head>
<body>
     <h1> Awardees </h1>
    <table>
        <thead>
            <tr>
              <th>Year</th>
              <th>Awardees</th>
              <th>Language</th>
          </tr>
        </thead>
        <tbody>
            {% for janapith in janapith_data %}
            <tr>
                <td>{{ janapith["year"] }}</td>
                <td>{{ janapith["awardees"] }}</td>
                <td>{{ janapith["language"] }}</td>
            </tr>
            {% endfor %}
          </tr>
        </tbody>
    </table>                    
</body>
</html>
"""
