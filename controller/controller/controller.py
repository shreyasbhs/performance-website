import pynecone as pc


class State(pc.State):
    
    pageload = "100"
    # @pc.var
    # def pageload(self):
    #     return
    def set_pageload(self,pageload):
        self.pageload = pageload


def index():
    return pc.vstack(
        pc.heading(
            "Performance metrics",
            color="red",
            text_align="left",
        ),
        pc.box(
        pc.vstack(    
        pc.text("Enter page load time"),
        pc.input(
            value = State.pageload,
            on_change = State.set_pageload
        )
        ),
        width="40%",
        left="5%"
        ),
        
    )

app = pc.App(state=State)

app.add_page(index, route = '/')
app.compile()