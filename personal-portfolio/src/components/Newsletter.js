import { Col, Row} from "react-bootstrap";
import navIcon1 from '../assets/img/nav-icon1.svg';

export const Newsletter = ({}) => {

  return (
    <Row className="newsletter-bx wow slideInUp">
      <Col lg={12}>
        <Row>
          <Col lg={8} md={8} xl={8} className="d-flex justify-content-end align-items-end">
            <h3>Let's connect <br />and find something inspiring together!</h3>
          </Col>
          <Col lg={4} md={4} xl={4} className="d-flex justify-content-center align-items-end">
            <div className="social-icon_2">
              <a href="https://www.linkedin.com/in/qi-niu-0596ab290/">
                <img src={navIcon1} alt="LinkedIn"/>
              </a>
            </div>
          </Col>
        </Row>
      </Col>
    </Row>
  )
}